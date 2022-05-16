from IGL_account.models import User
from rest_framework import serializers
from .models import Icon, IconTeam, IconTeamMember
from iconApi.settings.default import base_url

class IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = (
            'first_name', 'last_name', 'display_name', 'display_image', 'user',)


class IconTeamSerializer(serializers.ModelSerializer):
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = IconTeam
        fields = (
            'icon', 'team_name', 'display_image',)

    def get_display_image(self, obj):
        if obj:
            a = base_url + obj.display_image.url
            return a
        return ''


class IconTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = IconTeamMember
        fields = (
            "user", 'team', 'joined_at', 'left_at',)
