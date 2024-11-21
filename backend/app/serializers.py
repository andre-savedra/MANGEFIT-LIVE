from rest_framework import serializers
from .models import *
from rest_framework.serializers import ModelSerializer, SlugRelatedField, PrimaryKeyRelatedField, StringRelatedField

#CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    groups = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'groups', 'nome', )
        many = True

#Ingrediente
class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'
        many = True

#Salada
class SaladaReadSerializer(serializers.ModelSerializer):
    ingredientes = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nome',
    )
    class Meta:
        model = Salada
        fields = '__all__'
        many = True

class SaladaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salada
        fields = '__all__'
        many = True

#Salada_Avaliacao
class Salada_AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salada_Avaliacao
        fields = '__all__'
        many = True

#Pedido
class PedidoReadSerializer(serializers.ModelSerializer):
    usuarioFK = CustomUserSerializer()
    itens = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id','data_hora','usuarioFK','status','valor_entrega','valor_total','itens']
        many = True
    
    def get_itens(self, obj):
        itensSalvos = Item_Pedido.objects.filter(pedidoFK=obj)
        return Item_PedidoReadSaladSerializer(itensSalvos, many=True).data

class PedidoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        many = True

#Item_Pedido
class Item_PedidoReadSaladSerializer(serializers.ModelSerializer):
    saladaFK = SaladaReadSerializer()

    class Meta:
        model = Item_Pedido
        fields = '__all__'
        many = True

class Item_PedidoReadSerializer(serializers.ModelSerializer):
    saladaFK = SaladaReadSerializer()
    pedidoFK = PedidoReadSerializer()

    class Meta:
        model = Item_Pedido
        fields = '__all__'
        many = True

class Item_PedidoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Pedido
        fields = '__all__'
        many = True