

from django.urls import path 
from .views import SummerizeTxt, Summerize

urlpatterns = [
    path("", SummerizeTxt.as_view(), name = "summerize_txt"),
    path("summerize/", Summerize.as_view(), name = "summerize")
]