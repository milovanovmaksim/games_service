from django.db import models
from django.contrib.auth.models import User


class EsrbRating(models.Model):
    description = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('description', )

    def __str__(self) -> str:
        return self.description


class Game(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, unique=True)
    esrb_rating = models.ForeignKey(EsrbRating, related_name='games', on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    played_once = models.BooleanField(default=False)
    played_times = models.IntegerField(default=0)
    owner = models.ForeignKey(User, related_name='games', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Player(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'))

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)

    class Meta:
        ordering = ('name', )

    def __str__(self) -> str:
        return self.name


class PlayerScore(models.Model):
    player = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        ordering = ('-score', )
