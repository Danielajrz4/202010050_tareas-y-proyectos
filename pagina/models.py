from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    curso = models.CharField(max_length=200, null=True)
    descripcion = models.TextField(max_length=200, null=True)
    precio = models.FloatField()
    cupo = models.IntegerField(default=0, null=True, blank=True)
    imagen = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.curso
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except: 
            url =''
        return url
    
class Order(models.Model):
    Customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=True, null=True, blank=True)
    transaction_id=models.CharField(max_length=200, null=True)
    @property
    def ttotal(self):
        orderitems=self.orderitem_set.all()
        ttotal = sum([item.total for item in orderitems])
        return ttotal
    def __str__(self):
        return self.transaction_id
    
class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    data_added=models.DateTimeField(auto_now_add=True)
    @property
    def total(self):
        totall=self.product.precio
        return totall

class MetodoPago(models.Model):
    nombre=models.CharField(max_length=100,null=True, blank=True )
    email=models.EmailField(unique=True,null=True, blank=True)
    titular_de_la_tarjeta=models.CharField(max_length=100,null=True, blank=True)
    numero_de_tarjeta=models.BigIntegerField(null=True, blank=True)
    fecha_de_vencimiento=models.SmallIntegerField(null=True, blank=True)
    codigo_de_seguridad=models.SmallIntegerField(null=True, blank=True)


