from rest_framework import serializers
from IGL_account.models import User
from .models import Platform, Game, Tournament, StageType, Stage, Group, Round, Match, MatchParticipant, TrophyCategory, \
    BadgesCategory
from iconApi.settings.default import base_url


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = (
            'name', 'manufacturer', 'model',)


class GameSerializer(serializers.ModelSerializer):
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = (
            'id', 'display_name', 'slug', 'full_name', 'short_name', 'platforms', 'display_image',)

    def get_display_image(self, obj):
        if obj:
            a = base_url + obj.display_image.url
            return a
        return ''


class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = (
            'name', 'full_name', 'slug', 'game', 'size', 'scheduled_date_start', 'scheduled_date_end',)


class StageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageType
        fields = ('name',)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('name', 'tournament', 'number', 'stage_type', 'is_closed',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'tournament', 'closed',)


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ('tournament', 'stage', 'group', 'number', 'start_datetime', 'end_datetime',)


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            'tournament', 'round', 'stage', 'group', 'number', 'scheduled_datetime', 'start_datetime', 'end_datetime',
        )


class MatchParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchParticipant
        fields = ('user', 'tournament', 'match', 'checked_in_at',)


class TrophyCategorySerializer(serializers.ModelSerializer):
    """ A TrophyCategory Serializer is used for TrophyCategory Model """

    class Meta:
        """ Metaclass is used for changed the behaviour of Your TrophyCategory Model fields"""

        model = TrophyCategory
        fields = ('id', 'category_name',)


class BadgesCategorySerializer(serializers.ModelSerializer):
    """ A BadgesCategory Serializer is used for BadgesCategory Model """

    class Meta:
        """ Metaclass is used for changed the behaviour of Your  BadgesCategory Model fields"""

        model = BadgesCategory
        fields = ('id', 'category_id', 'badge_type', 'display_name', 'badges_image',)
