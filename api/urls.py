from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from authentication.views import login_view,logout_view,register_view,get_user_by_id
from room.views import post_ad,list_ads,user_ad_detail,user_ads_list_by_id,get_banner
# from addrooms.views import upload_room,list_rooms

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user/<int:pk>/', get_user_by_id, name='update_user'),


    path('post-ad/', post_ad, name='post-ad'),
    path('ads/view/',list_ads, name='list_ads'),
    path('ads/view/user/', list_ads, name='list_ads'),


    path('user/<int:user_id>/ads/', user_ads_list_by_id, name='user-ads-list-by-id'),
    path('user/ads/<int:pk>/', user_ad_detail, name='user-ad-detail'),

    path('api/banners/', get_banner, name='banner-list'),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)