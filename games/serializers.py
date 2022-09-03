from rest_framework import serializers
from django.contrib.auth.models import User

from .models import EsrbRating, Game, Player, PlayerScore

'''
class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    esrb_rating = serializers.CharField(max_length=150)
    played_once = serializers.BooleanField(required=False)
    played_times = serializers.IntegerField(required=False)

    def create(self, validate_data):
        return Game.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.esrb_rating = validated_data.get('esrb_rating', instance.esrb_rating)
        instance.played_once = validated_data.get('played_once', instance.played_once)
        instance.played_times = validated_data.get('played_times', instance.played_times)
        instance.save()
        return instance
'''


class GameSerializer(serializers.HyperlinkedModelSerializer):
    #  created_timestamp = serializers.DateTimeField(read_only=True)
    esrb_rating = serializers.SlugRelatedField(queryset=EsrbRating.objects.all(),
                                               slug_field='description')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Game
        fields = (
            'url',
            'esrb_rating',
            'name',
            'release_date',
            'played_once',
            'played_times',
            'owner'
        )


class EsrbRatingSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(many=True,
                                                read_only=True,
                                                view_name='game-detail')

    class Meta:
        model = EsrbRating
        fields = ('url', 'id', 'description', 'games', )


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = (
            'url',
            'id',
            'score',
            'score_date',
            'game'
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Player
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'scores'
        )


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = ('url', 'id', 'score', 'score_date', 'player', 'game')


class UserGameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'games')
