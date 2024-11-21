from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAuthenticatedOrReadOnly
from django.core.exceptions import PermissionDenied
from .customFilters import *
from .customSerializer import *
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

class IngredienteView(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]    
    ordering_fields = '__all__'
    # permission_classes = (IsAuthenticatedOrReadOnly,)   

class SaladaView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Salada.objects.all()
    write_serializer_class = SaladaWriteSerializer
    read_serializer_class = SaladaReadSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]    
    ordering_fields = '__all__'
    # permission_classes = (IsAuthenticatedOrReadOnly,)   

class Salada_AvaliacaoView(APIView):    
    # permission_classes = (IsAuthenticatedOrReadOnly,)   

    def post(self, request):
        saladaFK = request.data.get("saladaFK",0)
        nota = request.data.get("avaliacao",0)
        salada = None
        try:
            salada = Salada.objects.get(id=saladaFK)           

            saladaAvaliacao = Salada_Avaliacao.objects.get(saladaFK=salada.id)
            saladaAvaliacao.soma_avaliacao += nota
            saladaAvaliacao.numero_avaliacoes += 1
            saladaAvaliacao.save()

            return Response(status=200,data='Avaliação salva com sucesso!')

        except Salada.DoesNotExist:            
            return Response(status=404, data='Salada não encontrada!')
        
        except Salada_Avaliacao.DoesNotExist:
            novaAvaliacao = Salada_Avaliacao()
            novaAvaliacao.saladaFK = salada
            novaAvaliacao.numero_avaliacoes = 1
            novaAvaliacao.soma_avaliacao = nota
            novaAvaliacao.save()
            return Response(status=200, data='Avaliação criada com sucesso!')
            


class PedidoView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Pedido.objects.all()
    write_serializer_class = PedidoWriteSerializer
    read_serializer_class = PedidoReadSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]    
    ordering_fields = '__all__'
    # permission_classes = (IsAuthenticated,)   

    def get_queryset(self):
        user = self.request.user
        queryset = Pedido.objects.all()
        if user is None:
            return queryset
        
        # if not user.is_superuser:
            # queryset = Pedido.objects.filter(usuarioFK__email=user.username)
                    
        return queryset 
    
    def create(self, request, *args, **kwargs):
        user = None
        data = request.data
        valor_entrega = data.get("valor_entrega",0)
        itens = data.get("itens",[])

        try:
            user = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response(status=404, data='Usuário não encontrado!')
        
        if user is None:
            return Response(status=404, data='Usuário não encontrado!')
        
        novoPedido = Pedido()
        novoPedido.usuarioFK = user
        novoPedido.valor_entrega = valor_entrega
        novoPedido.save()
        itensSalvos = []
        if novoPedido is None:
            return Response(status=500, data='Erro ao salvar pedido!')
        
        try:
            #salvando itens
            for item in itens:                
                saladaFK = item["saladaFK"]                
                quantidade = item["quantidade"]
                observacao = item["observacao"]
                salada = Salada.objects.get(id=saladaFK)

                novoItemPedido = Item_Pedido()
                novoItemPedido.saladaFK = salada
                novoItemPedido.pedidoFK = novoPedido
                novoItemPedido.quantidade = quantidade
                novoItemPedido.observacao = observacao
                novoItemPedido.save()

                if novoItemPedido is None:
                    return Response(status=500, data='Erro ao salvar item do pedido!')

                itemSerialized = Item_PedidoReadSerializer(novoItemPedido, many=False)
                itensSalvos.append(itemSerialized.data)
            novoPedidoSerialized = PedidoReadSerializer(novoPedido, many=False)
            return Response(status=200,data=novoPedidoSerialized.data)

        except Salada.DoesNotExist:            
            return Response(status=404, data='Salada não encontrada!')


    def update(self, request, *args, **kwargs):
        pedidoId = kwargs.get('pk')
        user = None
        data = request.data
        valor_entrega = data.get("valor_entrega",0)
        itens = data.get("itens",[])

        try:
            user = CustomUser.objects.get(id=request.user.id)
        except CustomUser.DoesNotExist:
            return Response(status=404, data='Usuário não encontrado!')
        
        if user is None:
            return Response(status=404, data='Usuário não encontrado!')
        
        novoPedido = None

        try:
            novoPedido = Pedido.objects.get(id=pedidoId)
            novoPedido.usuarioFK = user
            novoPedido.valor_entrega = valor_entrega
            novoPedido.save()
        except Pedido.DoesNotExist:
            return Response(status=404, data='Pedido não encontrado!')
        
        itensSalvos = []
        if novoPedido is None:
            return Response(status=500, data='Erro ao salvar pedido!')
        
        #substituir
        itensAntigos = Item_Pedido.objects.filter(pedidoFK=novoPedido.id)
        itensAntigos.all().delete()
        try:
            #salvando itens
            for item in itens:                
                saladaFK = item["saladaFK"]                
                quantidade = item["quantidade"]
                observacao = item["observacao"]
                salada = Salada.objects.get(id=saladaFK)

                novoItemPedido = Item_Pedido()
                novoItemPedido.saladaFK = salada
                novoItemPedido.pedidoFK = novoPedido
                novoItemPedido.quantidade = quantidade
                novoItemPedido.observacao = observacao
                novoItemPedido.save()

                if novoItemPedido is None:
                    return Response(status=500, data='Erro ao salvar item do pedido!')

                itemSerialized = Item_PedidoReadSerializer(novoItemPedido, many=False)
                itensSalvos.append(itemSerialized.data)
            novoPedidoSerialized = PedidoReadSerializer(novoPedido, many=False)
            return Response(status=200,data=novoPedidoSerialized.data)

        except Salada.DoesNotExist:            
            return Response(status=404, data='Salada não encontrada!')

class Item_PedidoView(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Item_Pedido.objects.all()
    write_serializer_class = Item_PedidoWriteSerializer
    read_serializer_class = Item_PedidoReadSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]    
    ordering_fields = '__all__'
    # permission_classes = (IsAuthenticated,)     


