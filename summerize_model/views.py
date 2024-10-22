from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .services import TransformerService

transformer_service = TransformerService()


@api_view(['POST'])
def summerize_text(request):
    try:
        text = request.data.get('text')
        if not text:
            return Response({'message':"No text found"}, status=status.HTTP_204_NO_CONTENT)
        summary = transformer_service.summarize(text)
        return Response({'message':summary}, status=status.HTTP_200_OK)
    except Exception as error:
        return Response({'message':str(error)}, status=status.HTTP_400_BAD_REQUEST)

