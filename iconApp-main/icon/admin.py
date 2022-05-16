from django.contrib import admin

from .models import (
    Icon,
    IconTeam,
    IconTeamMember,
)

admin.site.register(Icon)
admin.site.register(IconTeam)
admin.site.register(IconTeamMember)
