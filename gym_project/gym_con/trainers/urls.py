from django.urls import path
from . views import TrainersPageView


urlpatterns = [
    path('', TrainersPageView.as_view(), name="trainers"),
]