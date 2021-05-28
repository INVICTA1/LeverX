from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, logout, login
from .serializer import LoginSerializer, RegistrationSerializer, UserSerializer
from django.contrib.auth import get_user_model
from .permissions import IsOwnerProfileOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserViewList(generics.ListAPIView):
    # permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = authenticate(username=request.data.get('email'), password=request.data.get('password'))
        login(self.request, user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=request.data.get('email'), password=request.data.get('password'))
        login(self.request, user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated, IsOwnerProfileOrReadOnly)

    def get(self, request):
        if request.user.is_authenticated():

            print(request)
        print(request.user)
        return Response( status=status.HTTP_200_OK)

        # logout(request.user)
