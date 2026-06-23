from django.db import models


class Parroquia(models.Model):

    nombre = models.CharField(max_length=100)

    UBICACIONES = [
        ('Norte', 'Norte'),
        ('Sur', 'Sur'),
        ('Este', 'Este'),
        ('Oeste', 'Oeste')
    ]

    TIPOS = [
        ('Urbana', 'Urbana'),
        ('Rural', 'Rural')
    ]

    ubicacion = models.CharField(
        max_length=20,
        choices=UBICACIONES
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    def __str__(self):
        return self.nombre


class Barrio(models.Model):

    nombre = models.CharField(max_length=100)

    numero_viviendas = models.IntegerField()

    PARQUES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6')
    ]

    numero_parques = models.IntegerField(
        choices=PARQUES
    )

    numero_edificios_residenciales = models.IntegerField()

    parroquia = models.ForeignKey(
        Parroquia,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre


class PresidenteBarrio(models.Model):

    cedula = models.CharField(max_length=10)

    nickname = models.CharField(max_length=50)

    edad = models.IntegerField()

    profesion = models.CharField(max_length=100)

    barrio = models.OneToOneField(
        Barrio,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nickname