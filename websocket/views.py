from django.core.checks import messages
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage, Connection
import boto3
import json

# Create your views here.


def _parse_body(body):
    body_unicode = body.decode('utf-8')
    return json.loads(body_unicode)


def _send_to_connection(connection_id, data):
    gatewayapi = boto3.client('apigatewaymanagementapi', endpoint_url='https://9oaktw3efg.execute-api.us-east-2.amazonaws.com/test/',
                              region_name='us-east-2', aws_access_key_id='AKIAJNUEHAK6LZAF5LLA', aws_secret_access_key='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')
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=json.dumps(data).encode('utf-8'))


@csrf_exempt
def test(request):
    return JsonResponse({'message': 'hello Daud'}, status=200)


@csrf_exempt
def connect(request):
    body = _parse_body(request.body)
    Connection.objects.create(connection_id=body['connectionId'])
    # return JsonResponse({'message': 'connected succussfully'}, status=200)


@csrf_exempt
def disconnect(request):
    body = _parse_body(request.body)
    Connection.objects.get(connection_id=body['connectionId']).delete()
    # return JsonResponse({'message': 'disconnected succussfully'}, status=200)


@csrf_exempt
def send_message(request):
    body = _parse_body(request.body)
    print(body)
    ChatMessage.objects.create(message=body["body"]["content"], username=body["body"]["username"], timestamp=body["body"]["timestamp"])
    data = {'messages': [body]}
    connections = Connection.objects.all()
    for connection in connections:
        _send_to_connection(str(connection), data)
    # return JsonResponse({'message': data}, status=200)

@csrf_exempt
def get_messages(request):
    messages = [ obj.as_dict() for obj in ChatMessage.objects.all() ]
    data = {'messages': messages}
    connections = Connection.objects.all()
    for connection in connections:
        _send_to_connection(str(connection), data)
    # return JsonResponse({'messages': data})
