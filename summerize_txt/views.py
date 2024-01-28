from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
import requests

# Create your views here.

class SummerizeTxt(View):
    def get(self, request):
        return render(request, 'summerize_txt/index.html')

class Summerize(SummerizeTxt):
    
    url = "https://open-ai21.p.rapidapi.com/summary"
    headers = {
        "content-type": "application/json",
	    "X-RapidAPI-Key": "aae89c5f80msh780b5cd7b24f4b1p13e122jsn3e90482eb1b7",
        "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }

    def get(self, request):
        if request.method == 'GET':
            txt = request.GET.get('text_input', "")
            payload = { "text": txt }
            response = requests.post(Summerize.url, json=payload, headers=Summerize.headers)

            if response.status_code == 200:
                  result = response.json()
                  result = result["result"]
            else:
                 print(f"Error: {response.status_code}, {response.text}")

            print(txt)
            return HttpResponse(result)
