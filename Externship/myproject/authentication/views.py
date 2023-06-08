from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer


@api_view(["POST"])
def login(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.validated_data["user"]
    refresh = RefreshToken.for_user(user)

    return Response({"refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout(request):
    # Perform any logout logic here if needed
    return Response(status=status.HTTP_204_NO_CONTENT)
