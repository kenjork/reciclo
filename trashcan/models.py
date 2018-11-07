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



#


