from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from authentication.views import login_view,logout_view,register_view
from room.views import post_ad,list_ads
# from addrooms.views import upload_room,list_rooms

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    path('post-ad/', post_ad, name='post-ad'),
    path('ads/view/', list_ads, name='list_ads'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)