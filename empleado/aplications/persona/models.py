from django.db import models
from aplications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=20)

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades Empleados'


    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    """Modelo para tabla empleado"""
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    # Contador
    # Administrador
    # Economista
    # Otro
    first_name = models.CharField('Nombres', max_length=50)
    last_name = models.CharField('Apellidos', max_length=70)
    full_name = models.CharField(
        'Nombre Completo',
        max_length=60,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES, default='3')
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to='media/empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name='Mi Personal'
        verbose_name_plural='Empleados de la Empresa'
        ordering = ['last_name']
        unique_together = ('first_name','last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name


