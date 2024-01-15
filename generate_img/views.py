from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import requests

# Create your views here.
class GenerateImg(View):
    def get(self, request):
        return render(request, 'generate_img/index.html')

class Generate(GenerateImg):

    url = "https://chatgpt-42.p.rapidapi.com/texttoimagetv"

    headers = {
        "content-type": "application/json",
        'X-RapidAPI-Key': 'aae89c5f80msh780b5cd7b24f4b1p13e122jsn3e90482eb1b7',
        "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
    }

    def get(self, request):
        if request.method == 'GET':
            txt = request.GET.get('text_input', "")
            payload = { "text": txt }
            response = requests.post(Generate.url, json=payload, headers=Generate.headers)
            
            if response.status_code == 200:
                  result = response.json()
                  result = result["generated_image"]
            else:
                 print(f"Error: {response.status_code}, {response.text}")

            print(result)
            return HttpResponse(result)
