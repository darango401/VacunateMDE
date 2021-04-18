from django.db import models
from django.db.models.enums import Choices
from django.core.exceptions import ValidationError


# Create your models here.

DOCUMENTOS = [
        ('RC', 'Registro Civil'),
        ('TI', 'Tarjeta de identidad'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('PA', 'Pasaporte'),
        ('MS', 'Menor sin identidad'),
        ('AS', 'Adulto sin identidad'),
        ]

GENERO = [
    ('F', 'Femenino'),
    ('M', 'Masculino')
    ]

COMUNAS = [
    ('1 - Popular', 'Comuna 1 - Popular'),
    ('2 - Santa Cruz', 'Comuna 2 - Santa Cruz'),
    ('3 - Manrique', 'Comuna 3 - Manrique'),
    ('4 - Aranjuez', 'Comuna 4 - Aranjuez'),
    ('5 - Castilla', 'Comuna 5 - Castilla'),
    ('6 - Doce de Octubre', 'Comuna 6 - Doce de Octubre'),
    ('7 - Robledo', 'Comuna 7 - Robledo'),
    ('8 - Villa Hermosa', 'Comuna 8 - Villa Hermosa'),
    ('9 - Buenos Aires', 'Comuna 9 - Buenos Aires'),
    ('10 - La Candelaria', 'Comuna 10 - La Candelaria'),
    ('11 - Laureles-Estadio', 'Comuna 11 - Laureles-Estadio'),
    ('12 - La América', 'Comuna 12 - La América'),
    ('13 - San Javier', 'Comuna 13 - San Javier'),
    ('14 - El Poblado', 'Comuna 14 - El Poblado'),
    ('15 - Guayabal', 'Comuna 15 - Guayabal'),
    ('16 - Belén', 'Comuna 16 - Belén'),
    ]

BARRIOS = {
    COMUNAS[0]: [('H', 'Hola'),('M', 'Mundo')]
}

VACUNAS = [
        ('Pfizer', 'Pfizer/BioNtech'),
        ('AstraZeneca', 'AstraZeneca/Oxford'),
        ('Jansen', 'Jansen/Johnson & Johnson'),
        ]

class Vacunado(models.Model):
    # django-crispy-forms
    nombres=models.CharField(max_length=60)
    apellidos=models.CharField(max_length=60)
    tipo_documento=models.CharField('Tipo de documento', max_length=2, choices=DOCUMENTOS)
    numero_documento=models.CharField('Número de documento' ,max_length=10)
    fecha_nacimiento=models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False,
                            help_text="Por favor use el siguiente formato: <em>YYYY-MM-DD</em>.")
    genero=models.CharField(max_length=1, choices=GENERO, verbose_name="Género")
    correo_electronico=models.EmailField('Correo electrónico', max_length=120)
    comuna_residencia=models.CharField('Comuna de residencia', max_length=30, choices=COMUNAS)
    # barrio_residencia=models.CharField(max_length=30, choices=BARRIOS.get(comuna_residencia))
    telefono_fijo=models.CharField('Teléfono fijo', max_length=7, null=True, blank=True)
    telefono_movil=models.CharField('Teléfono movil', max_length=10)
    fecha_vacunacion=models.DateTimeField('Fecha de vacunación', auto_now=False, auto_now_add=False,
                            help_text="Por favor use el siguiente formato: <em>YYYY-MM-DD</em>.")
    vacuna_aplicada=models.CharField(max_length=30, choices=VACUNAS)
    # fecha_prox_vacuna
    Lote=models.CharField('Lote de vacuna', max_length=20)
    segunda_vacuna=models.BooleanField('Segunda vacuna aplicada')
    # EPS

    def __str__(self):
        return '%s %s' % (self.nombres, self.correo_electronico)