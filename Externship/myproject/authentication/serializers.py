from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(request=self.context.get("request"), email=email, password=password)

            if not user:
                raise serializers.ValidationError("Invalid email or password.", code="authorization")

            attrs["user"] = user
            return attrs

        raise serializers.ValidationError("Email and password are required.", code="authorization")
