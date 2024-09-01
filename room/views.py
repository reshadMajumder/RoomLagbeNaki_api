from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Ad, AdImage
from .serializers import AdSerializer, AdImageSerializer






#=======================ad post start================



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_ad(request):
    serializer = AdSerializer(data=request.data)
    if serializer.is_valid():
        ad = serializer.save(user=request.user)

        # Handle image uploads
        images_data = request.FILES.getlist('images')
        for image_data in images_data:
            ad_image = AdImage.objects.create(image=image_data)
            ad.images.add(ad_image)

        ad.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#=======================ad post end================



#=======================ad list start================
@api_view(['GET'])
def list_ads(request):
    try:
        ads = Ad.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)  # Print the exception to the server logs
        return Response({"error": "Failed to retrieve ads"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#=======================ad list end================

#=======================show ads by user start================

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_ad_detail(request, pk):

    try:
        
        ad = Ad.objects.get(pk=pk, user=request.user)
    except Ad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = AdSerializer(ad)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdSerializer(ad, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_ads_list_by_id(request, user_id):
    ads = Ad.objects.filter(user_id=user_id)
    serializer = AdSerializer(ads, many=True)
    return Response(serializer.data)
    #=======================show ads by user end================