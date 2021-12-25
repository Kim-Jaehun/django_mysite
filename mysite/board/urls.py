from django.urls import path
from . import views
from .views import (BoardListAPI, BoardDetailAPI)


urlpatterns = [
    path('detail/<int:pk>/', views.board_detail),
    path('list/', views.board_list),
    path('write/', views.board_write),

    path('api/product/', BoardListAPI.as_view()),
    path('api/product/<int:pk>/', BoardDetailAPI.as_view())
]
