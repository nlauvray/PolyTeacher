from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        
        
        
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

class FrenchItalianTranslationViewSet(APIView):

    def get(self, request):

        data = Translation.objects.all()
        serialized_data = TranslationSerializer(data, many=True)

        return Response(data=serialized_data.data, status=None)

class AllTranslation(APIView):

    def get(self, request):

        data = Translation.objects.all() # select * from translation
        serialized_data = TranslationSerializer(data, many=True) # formattage des données

        return Response(data=serialized_data.data, status=None) # affichage des données sous forme de réponse

def index(request):
    return render(request, 'index.html', context={})

def contact(request):
    return render(request, 'contact.html', context={})