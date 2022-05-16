from django.db import models
from IGL_account.models import User
from autoslug import AutoSlugField

from iconApi.models import BaseModel
from iconApi.mixins import AuditTrailMixin, GuidFieldMixin, ApiMappableMixin
from icon.models import Icon


class Platform(BaseModel):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def get_games(self):
        return Game.objects.filter(platforms=self)

    def __str__(self):
        return self.name


class Game(BaseModel,
           GuidFieldMixin):
    display_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='full_name', unique=True)
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    platforms = models.ManyToManyField(Platform)
    display_image = models.ImageField(default='call-of-duty.jpeg', upload_to='game_logos', blank=True, null=True)

    def get_platforms(self):
        return self.platforms.all()

    def __str__(self):
        return self.display_name


class Tournament(BaseModel,
                 AuditTrailMixin,
                 GuidFieldMixin,
                 ApiMappableMixin):
    name = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='full_name', unique_with='scheduled_date_start')
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    size = models.PositiveSmallIntegerField()
    scheduled_date_start = models.DateField()
    scheduled_date_end = models.DateField()

    def __str__(self):
        return self.name


class StageType(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Stage(BaseModel,
            AuditTrailMixin,
            GuidFieldMixin,
            ApiMappableMixin):
    name = models.CharField(max_length=255)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    stage_type = models.ForeignKey(StageType, blank=True, null=True, on_delete=models.SET_NULL)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - Stage {1}".format(self.tournament.name,
                                        self.name)


class Group(BaseModel,
            AuditTrailMixin,
            GuidFieldMixin,
            ApiMappableMixin):
    name = models.CharField(max_length=255)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return "{0} - Group {1}".format(
            self.tournament.name,
            self.name,
        )


class Round(BaseModel,
            AuditTrailMixin,
            GuidFieldMixin,
            ApiMappableMixin):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    number = models.PositiveSmallIntegerField()

    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{0} - Stage {1} - Group {2} - Round {3}".format(
            self.tournament.name,
            self.stage.name,
            self.group.name,
            self.number
        )


class Match(BaseModel,
            AuditTrailMixin,
            GuidFieldMixin,
            ApiMappableMixin):
    class Meta:
        verbose_name_plural = 'Matches'

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE, blank=True, null=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    number = models.PositiveSmallIntegerField()
    scheduled_datetime = models.DateTimeField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{0} - Round {1} - Match {2}".format(self.tournament.name,
                                                    self.round.number,
                                                    self.number)


class MatchParticipant(BaseModel,
                       GuidFieldMixin,
                       ApiMappableMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    checked_in_at = models.DateTimeField()

    def __str__(self):
        return self.user.username


class TrophyCategory(BaseModel,
                     AuditTrailMixin,
                     GuidFieldMixin,
                     ApiMappableMixin):
    """ A class is used to represent the TrophyCategory """
    category_name = models.CharField(max_length=225)

    def __str__(self):
        return self.category_name


class BadgesCategory(BaseModel,
                     AuditTrailMixin,
                     GuidFieldMixin,
                     ApiMappableMixin):
    """ A class is used to represent the TrophyCategory """
    category_id = models.ForeignKey(TrophyCategory, on_delete=models.CASCADE)
    badge_type = models.CharField(max_length=225)
    display_name = models.CharField(max_length=225)
    badges_image = models.ImageField(upload_to='badges_logos', blank=True, null=True)

    def __str__(self):
        return self.display_name

