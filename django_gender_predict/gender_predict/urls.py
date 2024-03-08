from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('gender-predict',views.home,name="home"),    
]
