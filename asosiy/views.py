from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class TopicAPIVIEW(APIView):
    def get(self,request):
        topic = Topic.objects.all()
        serializer = TopicSERIALIZER(topic, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AudiosAPIVIEW(APIView):
    def get(self,request):
        audios = Audio.objects.all()
        serializer = AudioSERIALIZER(audios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AUDIOAPIVIEWS(APIView):
    def get(self,request,pk):
        audio = Audio.objects.get(id=pk)
        serializer = AudioSERIALIZER(audio)
        return Response(serializer.data, status=status.HTTP_200_OK)



