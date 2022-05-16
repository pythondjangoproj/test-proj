from django.urls import path
from IGL_account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, \
    SendPasswordResetEmailView, UserPasswordResetView, IGLUsernameAPI
from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('igl_username/', IGLUsernameAPI.as_view(), name='igl_username'),
    path('igl_username/<int:pk>/', IGLUsernameAPI.as_view(), name='igl_username'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
