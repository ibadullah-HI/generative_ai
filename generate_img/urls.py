

from django.urls import path

from .views import GenerateImg, Generate

urlpatterns = [
    path("", GenerateImg.as_view(), name = "generate_img"),
    path("generate/", Generate.as_view(), name = "generate")
]

