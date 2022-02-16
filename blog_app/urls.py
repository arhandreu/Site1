from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<slug:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<slug:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<slug:slug>/', GetPost.as_view(), name='post')
]
