from django.urls import path
from icon.views import IconAPI, IconTeamAPI, IconTeamMemberAPI

urlpatterns = [
    path('icon/<int:pk>/', IconAPI.as_view(), name='icon'),
    path('icon/', IconAPI.as_view(), name='icon'),
    path('iconteam/', IconTeamAPI.as_view(), name='iconteam'),
    path('iconteammember/', IconTeamMemberAPI.as_view(), name='iconteammember'),
]
