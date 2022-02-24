from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from helper.helper import validateEmail


@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def candidate_token(request):
    # username = request.data.get("username")
    # password = request.data.get("password")
    # if username is None or password is None:
    #     return Response({'error': 'Please provide both username and password'},
    #                     status=HTTP_400_BAD_REQUEST)
    # user = authenticate(username=username, password=password)
    # if not user:
    #     return Response({'error': 'Invalid Credentials'},
    #                     status=HTTP_404_NOT_FOUND)
    return Response({'token': 'asdf'},
                    status=HTTP_200_OK)
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def home(request):
    email = request.data.get("email")
    password = request.data.get("password")
    # if username is None or password is None:
    #     return Response({'error': 'Please provide both username and password'},
    #                     status=HTTP_400_BAD_REQUEST)
    # user = authenticate(username=username, password=password)
    # if not user:
    #     return Response({'error': 'Invalid Credentials'},
    #                     status=HTTP_404_NOT_FOUND)
    # token, _ = Token.objects.get_or_create(user=user)
    val = validateEmail(email)
    return Response({'token': 'home',
        'val':val,
        'password':password},
                    status=HTTP_200_OK)