from django.urls import path
from . import views

urlpatterns = [
    path('list-news/', views.NewsListAPIView.as_view()),
    path('create-news/', views.NewsCreateAPIView.as_view()),
    path('detail-news/<int:pk>/', views.NewsRetrieveAPIView.as_view()),
    path('update-news/<int:pk>/', views.NewsUpdateAPIView.as_view()),
    path('delete-news/<int:pk>/', views.NewsDestroyAPIView.as_view()),
    path('rud-news/<int:pk>/', views.NewsRUDAPIView.as_view()),
]
