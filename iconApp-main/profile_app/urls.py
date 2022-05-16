from django.urls import path
from profile_app.views import UserPlatformAPI, UserGameAPI,UserMatchParticipantAPI

urlpatterns = [
    path('userplatform/<int:pk>/', UserPlatformAPI.as_view(), name='userplatform'),
    path('userplatform/', UserPlatformAPI.as_view(), name='userplatform'),
    path('userplatform/<int:pk>/', UserPlatformAPI.as_view(), name='userplatform'),
    path('usergame/<int:pk>/', UserGameAPI.as_view(), name='usergame'),
    path('usergame/', UserGameAPI.as_view(), name='usergame'),
    path('usermatchparticipants/', UserMatchParticipantAPI.as_view(), name='usermatchparticipants'),
]
