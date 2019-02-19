from rest_framework import serializers#, HyperLinkedIdentityField
from . models import Movies, Watchlists, MovieWatchlist, WatchlistTest, Users, AWS_link



class AWS_linkSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AWS_link
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = [
                'id',
                'title',
                'release_year',
                'poster_image_path',
        ]


class MovieWatchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieWatchlist
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = [
                'id',
                'name',
                'email',
                'avatar',
                'verified',
                'password',
        ]




class WatchlistSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, required=False)
    owner = UserSerializer(many=True, required=False)
    movie_watchlists = MovieWatchlistSerializer(many=True, required=False)
    
    class Meta:
        model = Watchlists
        # fields = '__all__'
        fields = [
                'id',
                'user_id',
                'type_id',
                'title',
                'cover',
                'description',
                'slug', 
                'is_public',
                'owner',
                'movie_watchlists',
                'movies',

        ]
        
class WatchlistTestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = WatchlistTest
        fields = '__all__'
        depth = 1



