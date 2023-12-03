from django.urls import path
from . import views

urlpatterns = [
    path("bank/", views.bank),
]