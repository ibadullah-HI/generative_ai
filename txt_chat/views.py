from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
import requests

# Create your views here.
class TxtChat(View):
    def get(self,request):
        return render(request, 'txt_chat/index.html')


class Chate(TxtChat):

    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4"


    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "aae89c5f80msh780b5cd7b24f4b1p13e122jsn3e90482eb1b7",
        "X-RapidAPI-Host": "chatgpt-42.p.rapidapi.com"
    }
    # url = "https://open-ai21.p.rapidapi.com/chatgpt"


    # headers = {
    #     "content-type": "application/json",
    #     "X-RapidAPI-Key": "6187173281msh4ccb5ce9a67f68fp115af7jsn99b8eec8b91e",
    #     "X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    # }


    def get(self, request):
        if request.method == 'GET':
            txt = request.GET.get('text_input', "")
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": txt
                    }
                ],
                "system_prompt": "",
                "temperature": 0.9,
                "top_k": 5,
                "top_p": 0.9,
                "max_tokens": 256,
                "web_access": False
            }
            # payload = {
            #     "messages": [
            #         {
            #             "role": "user",
            #             "content": txt
            #         }
            #     ],
            #     "web_access": False
            # }
            response = requests.post(Chate.url, json= payload, headers=Chate.headers)
            print(response.json())

            result = "sorry"
            if response.status_code == 200:
                  result = response.json()
                  result = result["result"]
            else:
                 print(f"Error: {response.status_code}, {response.text}")

            print(response)
            return HttpResponse(result)