from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TrashCan(models.Model):

    depth = models.FloatField(help_text='Profundidad del tacho.')

    barcode = models.CharField(
        max_length=100,
        null = True,
        blank = True,
    )

    lat = models.FloatField(
        null=True,
        blank = True,
    )
    lng = models.FloatField(
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length = 300,
        blank = True,
    )

    recyclers = models.ManyToManyField(
        User,
        through='Harvest',
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'trash_can'


class Level(models.Model):

    trash_can = models.ForeignKey(
        TrashCan, 
        related_name='levels',
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True,
    )

    distance = models.FloatField(
        help_text = 'Distancia del cesor a la basura cm'
    )
    
    class Meta:
        db_table = 'level'

    def __str__(self):
        return str(self.pk)

class Harvest(models.Model):

    #La relación de uno más mucho siempre tiene que estar los parametros. User, on_delete, related_name
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="Level",
    )

    trash_can = models.ForeignKey(
        TrashCan,
        on_delete=models.CASCADE,
        related_name="TrashCan",
    )

    date = models.DateField()

    STATUS = (
        (0, 'Por Recoger'),
        (1, 'Trabajo Hecho'),
    )

    status = models.BooleanField(
        max_length=50,
        choices=STATUS,
        default=0,
    )

    comment = models.TextField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'harvest'
        unique_together = ('user','trash_can','date')

#


