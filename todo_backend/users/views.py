# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import RegisterSerializer

# # class RegisterView(APIView):
# #     def post(self, request):
# #         serializer = RegisterSerializer(data=request.data)
# #         if serializer.is_valid():
# #             user = serializer.save()
# #             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.authtoken.models import Token

# # class RegisterView(APIView):
# #     def register_user(request):
# #         if request.method == 'POST':
# #             serializer = RegisterSerializer(data=request.data)
# #             if serializer.is_valid():
# #                 user = serializer.save()
# #                 token, created = Token.objects.get_or_create(user=user)  # ✅ Generate token
# #                 return Response({'token': token.key}, status=status.HTTP_201_CREATED)
# #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import RegisterSerializer

# class RegisterView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             # Generate JWT tokens for the newly registered user
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'token': str(refresh.access_token)  # Access token
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)

#         if user:
#             # Generate JWT token
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'token': str(refresh.access_token)  # Access token
#             }, status=status.HTTP_200_OK)

#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView  # ✅ Import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer



class RegisterView(APIView):
    permission_classes = [AllowAny]  # ✅ Allow anyone to register

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'token': str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]  # ✅ Allow anyone to login

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'token': str(refresh.access_token)
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
