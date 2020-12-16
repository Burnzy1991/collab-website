from django.urls import path, include
from . import views
from home.views import HomeView
urlpatterns = [
    path('', HomeView.as_view()),
]
