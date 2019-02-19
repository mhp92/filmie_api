from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movie', views.MovieViewSet)
router.register('movie_watchlist', views.MovieWatchlistViewSet)
router.register('watchlist', views.WatchlistViewSet, base_name='watchlist')
router.register('watchlist_test', views.WatchlistTestViewSet)
router.register('user', views.UserViewSet)
router.register('aws_link', views.AWS_linkViewSet)


urlpatterns = [
    path('', include(router.urls))
]
