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
