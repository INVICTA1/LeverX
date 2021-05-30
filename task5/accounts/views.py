from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializer import UserSerializer, LoginSerializer, UserAllSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewList(generics.ListAPIView):
    # permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserAllSerializer


class RegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        login(self.request, user)
        return Response(status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=request.data.get('email'), password=request.data.get('password'))
        login(self.request, user)
        return Response(status=status.HTTP_200_OK)
