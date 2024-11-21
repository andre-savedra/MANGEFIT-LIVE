from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import *
from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from decimal import Decimal

class CustomUser(AbstractBaseUser,PermissionsMixin):
    nome = models.CharField(max_length=150)
    email = models.EmailField("email address", unique=True)
    cpf = models.CharField(max_length=12, unique=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    rua = models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now)    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.email    


CATEGORIAS = [
    ('Clássicas','Clássicas'),
    ('Proteicas','Proteicas'),
    ('Veganas','Veganas'),
    ('Low Carb','Low Carb'),
    ('Detox','Detox'),
    ('Agridoces','Agridoces'),
]

class Ingrediente(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Salada(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    calorias = models.IntegerField()
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    peso = models.IntegerField()
    rendimento = models.IntegerField()
    categoria = models.CharField(max_length=100, choices=CATEGORIAS)
    ingredientes = models.ManyToManyField(Ingrediente)
    avaliacao = models.DecimalField(max_digits=4,decimal_places=2,default=0.0)
    
    def __str__(self):
        return self.nome

class Salada_Avaliacao(models.Model):
    saladaFK = models.ForeignKey(Salada, related_name="saladaAvaliacao_saladaFK", on_delete=models.CASCADE)    
    soma_avaliacao = models.DecimalField(max_digits=12,decimal_places=2)
    numero_avaliacoes = models.BigIntegerField()

    def __str__(self):
        return self.saladaFK.nome

@receiver(post_save, sender=Salada_Avaliacao)
def atualizar_avaliacao_salvar(sender, instance, **kwargs):
    salada = instance.saladaFK
    salada.avaliacao = 0.0
    if instance.numero_avaliacoes > 0:
        salada.avaliacao = instance.soma_avaliacao / instance.numero_avaliacoes
    salada.save()

@receiver(post_delete, sender=Salada_Avaliacao)
def atualizar_avaliacao_excluir(sender, instance, **kwargs):
    salada = instance.saladaFK
    salada.avaliacao = 0.0
    if instance.numero_avaliacoes > 0:
        salada.avaliacao = instance.soma_avaliacao / instance.numero_avaliacoes
    salada.save()

PEDIDO_STATUS = [
    ('Pendente','Pendente'),
    ('Aprovado','Aprovado'),
    ('Em produção','Em produção'),
    ('Em entrega','Em entrega'),
    ('Concluído','Concluído')
]


class Pedido(models.Model):
    data_hora = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    usuarioFK = models.ForeignKey(CustomUser, related_name="pedido_usuarioFK", on_delete=models.CASCADE)        
    status = models.CharField(max_length=150, choices=PEDIDO_STATUS, default="Pendente")
    valor_entrega = models.DecimalField(max_digits=10,decimal_places=2)    
    valor_total = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.usuarioFK.email
    
    def calculaTotalPedido(self):
        itens = Item_Pedido.objects.filter(pedidoFK=self.id)
        total = 0
        for item in itens:
            total += (item.saladaFK.preco * item.quantidade)
        return total + Decimal(self.valor_entrega)

    def save(self, *args, **kwargs):
        self.valor_total = Pedido.calculaTotalPedido(self)
        super(Pedido, self).save(*args, **kwargs)



class Item_Pedido(models.Model):
    saladaFK = models.ForeignKey(Salada, related_name="itemPedido_saladaFK", on_delete=models.CASCADE)
    pedidoFK = models.ForeignKey(Pedido, related_name="itemPedido_pedidoFK", on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    observacao = models.CharField(max_length=300,null=True,blank=True)


    def __str__(self):
        return self.saladaFK.nome


@receiver(post_save, sender=Item_Pedido)
def atualizar_total_pedido_salvar(sender, instance, **kwargs):
    pedido = instance.pedidoFK
    pedido.valor_total = pedido.calculaTotalPedido()
    pedido.save()

@receiver(post_delete, sender=Item_Pedido)
def atualizar_total_pedido_excluir(sender, instance, **kwargs):
    pedido = instance.pedidoFK
    pedido.valor_total = pedido.calculaTotalPedido()
    pedido.save()