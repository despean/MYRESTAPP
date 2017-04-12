from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from simpleapi.models import Trending
from simpleapi.tweetcollections import *
from simpleapi.serializers import TrendsSerializers


# Create your views here.

@csrf_exempt
def all_trens(request):
    if request.method == 'GET':
        trens = Trending.objects.all()
        serializer = TrendsSerializers(trens, many=True)
        return JsonResponse(serializer.data, safe=False)


def given_trend(request, id):
    try:
        trend = Trending.objects.get(pk=id)
    except Trending.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TrendsSerializers(trend)
        return JsonResponse(serializer.data)

def scrap(request):
    tweet_collection(Trending)
    print('--------------------Done!!!----------------------')
    return JsonResponse({"report":"Done","Status":200, "url":"http://127.0.0.1:8000/api/v1/trends"}, safe=False)
