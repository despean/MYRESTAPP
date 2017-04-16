from simpleapi.models import Trending
from simpleapi.tweetcollections import *
from simpleapi.serializers import TrendsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions

# Create your views here.

@api_view(['GET'])
def all_trens(request, format=None):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    if request.method == 'GET':
        trens = Trending.objects.all()[500:2000]
        serializer = TrendsSerializers(trens, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def given_trend(request, id, format ='xml'):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    try:
        trend = Trending.objects.get(tweet_id=id)
    except Trending.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = TrendsSerializers(trend)
        return Response(serializer.data)

@api_view(['GET'])
def scrap(request):
    tweet_collection(Trending)
    print('--------------------Done!!!----------------------')
    return JsonResponse({"report":"Done","Status":200, "url":"http://127.0.0.1:8000/api/v1/trends"})
