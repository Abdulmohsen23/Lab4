from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:number>", views.anyNumber, name="anynumber"),
    path("taxrate/", views.taxRate, name="taxrate"),
    
]