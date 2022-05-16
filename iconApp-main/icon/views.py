from django.shortcuts import render
from rest_framework.response import Response
from IGL_account.models import User
from .serializer import IconSerializer, IconTeamSerializer, IconTeamMemberSerializer
from rest_framework import generics
from .models import Icon, IconTeam, IconTeamMember


# Create your views here.

class IconAPI(generics.GenericAPIView):
    serializer_class = IconSerializer

    def post(self, request):
        try:
            serializer = IconSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create icon"})

    def get(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = Icon.objects.get(id=user_id)
                serializer = IconSerializer(user)
                return Response({"data": serializer.data})
            user = Icon.objects.all()
            serializer = IconSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to get the Icon details"})


class IconTeamAPI(generics.GenericAPIView):
    serializer_class = IconTeamSerializer

    def post(self, request):
        try:
            serializer = IconTeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to create the Icon team details"})

    def get(self, request, pk=None):
        try:
            user = IconTeam.objects.all()
            serializer = IconTeamSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to find Icon team details"})


class IconTeamMemberAPI(generics.GenericAPIView):
    serializer_class = IconTeamMemberSerializer

    def post(self, request):
        try:
            serializer = IconTeamMemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to update the Team member registration"})

    def get(self, request, pk=None):
        user_id = pk
        try:
            if user_id is not None:
                user = IconTeamMember.objects.get(id=user_id)
                serializer = IconTeamMemberSerializer(user)
                return Response({"data": serializer.data})
            user = IconTeamMember.objects.all()
            serializer = IconTeamMemberSerializer(user, many=True)
            return Response({"data": serializer.data})
        except:
            return Response({"message": "Unable to find team member details"})
