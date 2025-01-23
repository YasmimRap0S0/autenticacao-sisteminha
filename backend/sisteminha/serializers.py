from rest_framework import serializers
from .models import Desenvolvedor, Microempreendedor, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'perfil']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class DesenvolvedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Desenvolvedor
        fields = ['user', 'cpf', 'foto', 'github', 'descricao'] 
        extra_kwargs = {'password': {'write_only': True}}

        user = UserSerializer()
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)      
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()

        desenvolvedor = Desenvolvedor.objects.create(user=user, **validated_data)
        return desenvolvedor


class MicroempreendedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Microempreendedor
        fields = ['user', 'cnpj', 'foto']
        extra_kwargs = {'password': {'write_only': True}}

        user = UserSerializer()
    

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)      
        user_serializer.is_valid(raise_exception=True)

        user = user_serializer.save()

        microempreendedor = Microempreendedor.objects.create(user=user, **validated_data)
        return microempreendedor