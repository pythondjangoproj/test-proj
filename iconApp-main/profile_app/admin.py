from django.contrib import admin
from profile_app.models import UserPlatform, UserGame, UserMatchParticipant


# Register your models here.
class UserPlatformAdmin(admin.ModelAdmin):
    list_display = ['user_id']


admin.site.register(UserPlatform, UserPlatformAdmin)


class UserGameAdmin(admin.ModelAdmin):
    list_display = ['gammer_tag']


admin.site.register(UserGame, UserGameAdmin)


class UserMatchParticipantAdmin(admin.ModelAdmin):
    list_display = ['usermatchparticipant_id']


admin.site.register(UserMatchParticipant, UserMatchParticipantAdmin)
