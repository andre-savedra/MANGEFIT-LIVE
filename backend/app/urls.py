from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'ingredientes',IngredienteView)
router.register(r'saladas',SaladaView)
router.register(r'pedidos',PedidoView)
router.register(r'pedidos-itens',Item_PedidoView)

urlpatterns = router.urls
urlpatterns.append( path('avaliacao-salada/', Salada_AvaliacaoView.as_view(), name='avaliacao-salada'))
