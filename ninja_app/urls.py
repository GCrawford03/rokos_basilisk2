from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('register', views.register),
    path('logout', views.logout),
    path('game', views.index),
    path('get_rations', views.get_rations),
    path('process', views.game),
    path('reset', views.reset),
    path('textgame', views.game),
    path('train', views.train),
    path('war', views.war)
]