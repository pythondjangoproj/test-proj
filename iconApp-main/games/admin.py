from django.contrib import admin

from .models import (
    Platform,
    Game,
    Match,
    Round,
    Stage,
    MatchParticipant,
    Tournament,
    TrophyCategory,
    BadgesCategory,
)


class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'get_games')


class GameAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'get_platforms',)


class MatchParticipantsAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Tournament)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Match)
admin.site.register(MatchParticipant, MatchParticipantsAdmin)
admin.site.register(Round)
admin.site.register(Stage)
admin.site.register(TrophyCategory)
admin.site.register(BadgesCategory)
