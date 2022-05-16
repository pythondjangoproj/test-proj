from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from IGL_account.renderers import UserRenderer
from rest_framework import generics
from IGL_account.serializer import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, \
    UserChangePasswordSerializer, SendPasswordResetEmailSerializer, UserPasswordResetSerializer, Igl_Username_Serializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from IGL_account.models import User
# from games.models import Platform, Game, Tournament, StageType, Stage, Group, Round, Match, MatchParticipant
# from games.serializer import PlatformSerializer, GameSerializer, TournamentSerializer, StageTypeSerializer, \
#     StageSerializer, \
#     GroupSerializer, RoundSerializer, MatchSerializer, MatchParticipantSerializer
# from icon.models import Icon, IconTeam, IconTeamMember
# from icon.serializer import IconSerializer, IconTeamSerializer, IconTeamMemberSerializer
# from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)


# Generate Token Manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# To perform the IGL user registration
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        try:
            serializer = UserRegistrationSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                token = get_tokens_for_user(user)
                return Response({'token': token, 'msg': 'Registration Successful'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to registered the user details"})


# to perform login operation for registered IGL user
class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        try:
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                user = authenticate(email=email, password=password)
                if user is not None:
                    token = get_tokens_for_user(user)
                    return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
                else:
                    return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}},
                                    status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to perform login operation with given credential"})


# To fetch the IGL User details
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            serializer = UserProfileSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to get the user Record"})


# TO change the IGL user password
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            serializer = UserChangePasswordSerializer(data=request.data, context={'user': request.user})
            if serializer.is_valid(raise_exception=True):
                return Response({'msg': 'Password Changed Successfully'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to change user password"})


# to send the reset password link on user email id
class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        try:
            serializer = SendPasswordResetEmailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response({'msg': 'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to send link on registered email id "})


# to reset the user password
class UserPasswordResetView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, uid, token, format=None):
        try:
            serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
            serializer.is_valid(raise_exception=True)
            return Response({'msg': 'Password Reset Successfully'}, status=status.HTTP_200_OK)
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to perform user reset password"})


# to get the and update the igl username details with default avatar
class IGLUsernameAPI(generics.GenericAPIView):
    serializer_class = Igl_Username_Serializer

    def get(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = User.objects.get(id=user_id)
                serializer = Igl_Username_Serializer(user)
                return Response({"data": serializer.data})
            user = User.objects.all()
            serializer = Igl_Username_Serializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            logging.info('Information incoming!')
            return Response({"message": "unable to get user details found"})

    def patch(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = User.objects.get(id=user_id)
                user.IGL_Username = request.data['IGL_Username']
                user.profile_image = request.data['profile_image']
                user.save()
                return Response({"message": "Successfully Update"})
        except:
            logging.info('Information incoming!')
            return Response({"message": "Unable to update user details"})



