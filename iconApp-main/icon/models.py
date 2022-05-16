from django.db import models
from IGL_account.models import User

from iconApi.models import BaseModel
from iconApi.mixins import AuditTrailMixin, GuidFieldMixin


class Icon(BaseModel,
           AuditTrailMixin,
           GuidFieldMixin):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    display_name = models.CharField(max_length=255)
    display_image = models.ImageField(upload_to='icon_logos', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.display_name


class IconTeam(BaseModel,
               AuditTrailMixin,
               GuidFieldMixin):

    icon = models.OneToOneField(Icon, on_delete=models.CASCADE)
    team_name = models.CharField('Team name', max_length=255)
    display_image = models.ImageField(upload_to='team_logos', blank=True, null=True)

    def __str__(self):
        return self.team_name


class IconTeamMember(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(IconTeam, on_delete=models.CASCADE)
    joined_at = models.DateTimeField()
    left_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username

