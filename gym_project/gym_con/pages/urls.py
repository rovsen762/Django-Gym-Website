from django.urls import path
from . import views
from pages.views import ContactView

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', ContactView.as_view(), name="contact"),
]
