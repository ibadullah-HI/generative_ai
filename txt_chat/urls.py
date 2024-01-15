
from django.urls import path
from . views import TxtChat, Chate

urlpatterns = [
    path("", TxtChat.as_view(), name = "Txtchat"),
    path("chate/", Chate.as_view(), name = "chate")
]