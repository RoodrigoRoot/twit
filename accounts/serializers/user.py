from rest_framework import serializers
from accounts.selectors import user_exists, user_email_exists, get_user
from accounts.models.exceptions import PasswordAreDifferentException, UsernameExistsException, EmailExistsException


class CreateUserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=10, min_length=4)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)

    def validate_password(self, password):
        data = self.get_initial()
        password2 = data.get("password2")
        if password != password2:
            raise PasswordAreDifferentException("Las contraseñas deben ser iguales")
        return password

    def validate_username(self, username):
        if user_exists(username):
            raise UsernameExistsException("El nombre de usuario ya existe")
        return username

    def validate_email(self, email):
        if user_email_exists(email):
            raise EmailExistsException("El correo ya está siendo usado por otra cuenta.")
        return email


class ReadDataUserSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=10, min_length=4)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    description = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    def get_followers_count(self, obj):
        user = get_user(obj.get("username"), True)
        return user.followers_count

    def get_description(self, obj):
        description = obj.get("description")
        if description:
            return description
        return ""


class UpdateDataUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=4, allow_null=True)
    first_name = serializers.CharField(max_length=50, allow_blank=True)
    last_name = serializers.CharField(max_length=50, allow_blank=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)

