from django.urls import path
from .views import Anasayfa
urlpatterns = [
    path('',Anasayfa.as_view(),name = "anasayfa"),

]

