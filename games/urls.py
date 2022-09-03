from django.urls import path

from . import views


urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('esrb-ratings/', views.EsrbRatingList.as_view(), name=views.EsrbRatingList.name),
    path('esrb-ratings/<int:pk>/', views.EsrbRatingDetail.as_view(), name=views.EsrbRatingDetail.name),
    path('games/', views.GameList.as_view(), name=views.GameList.name),
    path('games/<int:pk>/', views.GameDetail.as_view(), name=views.GameDetail.name),
    path('players/', views.PlayerList.as_view(), name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name=views.PlayerDetail.name),
    path('player-scores/', views.PlayerScoreList.as_view(), name=views.PlayerScoreList.name),
    path('player-scores/<int:pk>/', views.PlayerScoreDetail.as_view(), name=views.PlayerScoreDetail.name),
    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name)
]
