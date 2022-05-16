from .models import UserPlatform, UserGame, UserMatchParticipant
from IGL_account.models import User
from rest_framework import serializers


class UserPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlatform
        fields = (
            "id","user_id", 'platforms',)


class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGame
        fields = (
            "userplatform_id", 'gammer_tag', 'game', 'display_image',)


class UserMatchParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMatchParticipant
        fields = (
            "usermatchparticipant_id", 'tournament', 'match', 'checked_in_at',)
