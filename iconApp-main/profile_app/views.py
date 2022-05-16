from django.shortcuts import render
from .serializers import UserPlatformSerializer, UserGameSerializer, UserMatchParticipantSerializer
from .models import UserPlatform, UserGame, UserMatchParticipant
from rest_framework.response import Response
from rest_framework import generics


# Create your views here.


class UserPlatformAPI(generics.GenericAPIView):
    serializer_class = UserPlatformSerializer

    def post(self, request):
        try:
            serializer = UserPlatformSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = UserPlatform.objects.get(id=user_id)
            serializer = UserPlatformSerializer(user)
            return Response({"data": serializer.data})
        user = UserPlatform.objects.all()
        serializer = UserPlatformSerializer(user, many=True)
        return Response({"data": serializer.data})


class UserGameAPI(generics.GenericAPIView):
    serializer_class = UserGameSerializer

    def post(self, request):
        try:
            serializer = UserGameSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = UserGame.objects.get(id=user_id)
            serializer = UserGameSerializer(user)
            return Response({"data": serializer.data})
        user = UserGame.objects.all()
        serializer = UserGameSerializer(user, many=True)
        return Response({"data": serializer.data})


class UserMatchParticipantAPI(generics.GenericAPIView):
    serializer_class = UserMatchParticipantSerializer

    def post(self, request):
        try:
            serializer = UserMatchParticipantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data})
        except Exception as ex:
            print(str(ex))

    def get(self, request, pk=None):
        user_id = pk
        if user_id is not None:
            user = UserMatchParticipant.objects.get(id=user_id)
            serializer = UserMatchParticipantSerializer(user)
            return Response({"data": serializer.data})
        user = UserMatchParticipant.objects.all()
        serializer = UserMatchParticipantSerializer(user, many=True)
        return Response({"data": serializer.data})
