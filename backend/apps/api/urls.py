from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListIncident.as_view()),
    path('<int:pk>/', views.DetailIncident.as_view()),
]