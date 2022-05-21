
from django.urls import path
from . views import BlogPageView,BlogDetailView

urlpatterns = [
    path('', BlogPageView.as_view(), name='blogs'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog'),

]
