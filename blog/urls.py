from django.urls import path
from . import views

urlpatterns = [
	path('profile', views.index, name='index'),
	path('blogs', views.post_list, name='post_list'),
]