from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_game, name='start_game'),
    path('game/<int:screen_id>/', views.game_view, name='game'),
    path('end/', views.end_game, name='end_game'),
]
