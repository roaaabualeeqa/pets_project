
from django.contrib import admin
from django.urls import path
from .views import PetList, PetDetail

urlpatterns = [
    path('',PetList.as_view(), name="pet_list"),
    path('<int:pk>/', PetDetail.as_view(), name="pet_detail" ),
]
