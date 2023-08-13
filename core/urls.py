from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('male',views.male),
    path('female',views.female)
]