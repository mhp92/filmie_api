from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model # If used custom user model

from rest_framework import generics, mixins, viewsets
from rest_framework import serializers


from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from .permissions import IsOwnerOrReadOnly
from . models import Movies, MovieWatchlist, Watchlists, WatchlistTest, Users, AWS_link
from . serializers import MovieSerializer, MovieWatchlistSerializer, WatchlistSerializer, WatchlistTestSerializer, UserSerializer, AWS_linkSerializer

from . pagination import WatchListLimitOffsetPagination



class WatchlistTestViewSet(viewsets.ModelViewSet):
    queryset = WatchlistTest.objects.all()
    serializer_class = WatchlistTestSerializer

    def get_queryset(self):
        qs = WatchlistTest.objects.all()
        query = self.request.GET.get('user_id')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs 

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    # password = serializers.CharField(write_only=True)


    def get_queryset(self):
        qs = Users.objects.all()
        query = self.request.GET.get('name')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs 


  

# router/ & api/ doing the same 

############### using router and viewsets ###############

class AWS_linkViewSet(viewsets.ModelViewSet):
    queryset = AWS_link.objects.all()
    serializer_class = AWS_linkSerializer

    def get_queryset(self):
        qs = AWS_link.objects.all()
        query = self.request.GET.get('title')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs 


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = Movies.objects.all()
        query = self.request.GET.get('title')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs 




class MovieWatchlistViewSet(viewsets.ModelViewSet):
    queryset = MovieWatchlist.objects.all()
    serializer_class = MovieWatchlistSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = MovieWatchlist.objects.all()
        query = self.request.GET.get('watchlist_id')
        if query is not None:
            qs = qs.filter(watchlist_id__exact=query)
        return qs 


# Custom ViewSet

class WatchlistViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Watchlists.objects.all()
        serializer = WatchlistSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def get_queryset(self):
        qs = Watchlists.objects.all()
        query = self.request.GET.get('type_id')
        if query is not None:
            qs = qs.filter(type_id__exact=query)
        return qs 



# class WatchlistViewSet(viewsets.ModelViewSet):
#     queryset = Watchlists.objects.all()
#     serializer_class = WatchlistSerializer
#     # pagination_class = WatchListLimitOffsetPagination # see pagination.py
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_queryset(self):
#         qs = Watchlists.objects.all()
#         query = self.request.GET.get('type_id')
#         if query is not None:
#             qs = qs.filter(type_id__exact=query)
#         return qs 

#     # assing request.user to new created watchlist
#     # it works! user_id in watchlist is assigned by the logged in user, but filmie account is not connected now 
#     def perform_create(self, serializer):

#         user_id = self.request.user.id

#         serializer.save(user_id=user_id)



#     @action(detail=True, methods=['GET'])
#     def movies (self, request, pk=None):
    
#         watch_list = get_object_or_404(Watchlists, id=pk)
        
#         movie_ids = MovieWatchlist.objects.values_list('movie_id', flat=True).filter(watchlist_id=pk)
        
#         movies = Movies.objects.filter(id__in=movie_ids)

#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=200)


#     @action(detail=True, methods=['GET'])
#     def owner (self, request, pk=None):
        
#         watch_list = get_object_or_404(Watchlists, id=pk)
#         movie_id = watch_list.user_id
        
#         owner = Users.objects.filter(id=movie_id)

#         serializer = UserSerializer(owner, many=True)
#         return Response(serializer.data, status=200)
        





############### using generics and mixins ###############




# class MovieAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     lookup_field        = 'pk'
#     serializer_class    = MovieSerializer 



#     # we can use the search function to find everything with the type_id=2 for Movies created by users

#     def get_queryset(self):
#         qs = Movies.objects.all()
#         query = self.request.GET.get('title')
#         if query is not None:
#             qs = qs.filter(title__icontains=query)
#         return qs 


#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class MovieRudView(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field        = 'pk'
#     serializer_class    = MovieSerializer 

#     def get_queryset(self):
#         return Movies.objects.all()





# class MovieWatchlistAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     lookup_field        = 'pk'
#     serializer_class    = MovieWatchlistSerializer 



#     # we can use the search function to find everything with the type_id=2 for Movies created by users

#     def get_queryset(self):
#         qs = MovieWatchlist.objects.all()
#         query = self.request.GET.get('watchlist_id')
#         if query is not None:
#             qs = qs.filter(watchlist_id__exact=query)
#         return qs 


#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class MovieWatchlistRudView(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field        = 'pk'
#     serializer_class    = MovieWatchlistSerializer 

#     def get_queryset(self):
#         return MovieWatchlist.objects.all()






# class WatchlistAPIView(mixins.CreateModelMixin, generics.ListAPIView):
#     lookup_field        = 'pk'
#     serializer_class    = WatchlistSerializer 



#     # we can use the search function to find everything with the type_id=2 for Watchlists created by users

#     def get_queryset(self):
#         qs = Watchlists.objects.all()
#         query = self.request.GET.get('type_id')
#         if query is not None:
#             qs = qs.filter(type_id__exact=query)
#         return qs 


#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     # def perform_create(self, serializer):

#     #     user_id = self.request.user.id

#     #     serializer.save(user_id=user_id)


#     # def perform_create(self, serializer):
#     #     serializer.save(user_id=self.request.user)



# class WatchlistRudView(generics.RetrieveUpdateDestroyAPIView):
#     lookup_field        = 'pk'
#     serializer_class    = WatchlistSerializer 




#     def get_queryset(self):
#         return Watchlists.objects.all()
