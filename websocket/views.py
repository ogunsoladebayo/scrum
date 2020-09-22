from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage, Connection
import json

# Create your views here.
def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)
    
@csrf_exempt
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200)

@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    Connection.objects.create(connection_id=body['connectionId'])
    return JsonResponse({'message': 'connected succussfully'}, status=200)

@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    Connection.objects.get(connection_id=body['connectionId']).delete()
    return JsonResponse({'message': 'disconnected succussfully'}, status=200)
