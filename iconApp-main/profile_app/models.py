from django.db import models
from IGL_account.models import User
from games.models import Platform, Game, Tournament,Match
from iconApi.models import BaseModel
from iconApi.mixins import AuditTrailMixin, GuidFieldMixin, ApiMappableMixin


# Create your models here.

class UserPlatform(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    platforms = models.ManyToManyField(Platform)

    def __str__(self):
        return str(self.user_id)

    def get_platforms(self):
        return self.platforms.all()


class UserGame(models.Model):
    userplatform_id = models.ForeignKey(UserPlatform, on_delete=models.CASCADE)
    gammer_tag = models.CharField(max_length=255)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    display_image = models.ImageField(default='call-of-duty.jpeg', upload_to='game_logos', blank=True, null=True)

    def __str__(self):
        return self.gammer_tag


class UserMatchParticipant(models.Model):
    usermatchparticipant_id = models.ForeignKey(UserGame, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    checked_in_at = models.DateTimeField()

    def __str__(self):
        return str(self.usermatchparticipant_id)

# class UserIcon(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#


# class UserTournament(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     display_name = models.CharField(max_length=255)
#     tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
#     add more fields
#     def __str__(self):
#         return self.di
