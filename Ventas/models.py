from django.db import models
from Pacientes.models import Patients
from Usuarios.models import UserModuleProfile


DIS = [
    ('LE', "Lejos"),
    ('CE', "Cerca"),
]
SIDE = [
    ('IZ', "Izquierda"),
    ('DE', "Derecha"),
]
STATUS = [
    ('PN', "Pendiente"),
    ('PE', "Pedido"),
    ('TA', "Taller"),
    ('FI', "Finalizado"),
]
TIPE = [
    ('Tarjeta Crédito', "Tarjeta Crédito"),
    ('Tarjeta Débito', "Tarjeta Débito"),
    ('Billetera Virtual', "Billetera Virtual"),
    ('Efectivo', "Efectivo"),
]

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=80, null=True, blank=True)
    price = models.FloatField()

    is_glasses = models.BooleanField(default=False)
    distance = models.CharField(
        max_length=2, null=True, blank=True, choices=DIS)
    side = models.CharField(max_length=2, null=True, blank=True, choices=SIDE)
    frame = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Patients, null=True, blank=True,
                               on_delete=models.SET_NULL)
    article = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.SET_NULL)
    units = models.PositiveIntegerField(default=1)
    total = models.FloatField(null=True)

    seller = models.ForeignKey(UserModuleProfile, null=True, blank=True,
                               on_delete=models.SET_NULL)
    status = models.CharField(max_length=2, default='PN', choices=STATUS)
    tipe = models.CharField(max_length=20, default='Efectivo', choices=TIPE)
    date = models.DateField(auto_now_add=True)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} unidad/es de {} a ${}'.format(self.units, self.article, self.total)
