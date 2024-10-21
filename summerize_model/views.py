from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from .services import TransformerService
from .services import TransformerService





transformer_service = TransformerService()

@api_view(['POST'])
def summerize_text(request):
    text = request.data.get('text')
    summary = transformer_service.summarize(text)
    return Response({'message':summary})
# Create your views here.
