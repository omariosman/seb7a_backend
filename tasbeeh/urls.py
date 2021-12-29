from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
 
from .models import Zekr
 
urlpatterns = [
    path('get_first_zekr/', views.get_first_zekr, name="get_first_zekr"),
    path('get_all_zekr/', views.get_all_zekr, name="get_all_zekr"),
    path('post_new_zekr/', views.post_new_zekr, name="post_new_zekr"),
    path('delete_zekr/', views.delete_zekr, name="delete_zekr"),
    path('update_zekr/', views.update_zekr, name="update_zekr"),
    path('increment_counter/', views.increment_counter, name="increment_counter"),
    path('reset_counter/', views.reset_counter, name="reset_counter"),
    path('try_api/', views.try_api, name="try_api"),

    
]
