from django.contrib.auth.models import User
from django.db.models import Q
from django.db import models


# Create your models here.

class TrashCanQuerySet(models.QuerySet):

    def get_not_address(self):
        return self.filter(
            ~Q(address='') | ~Q(address__isnull = True),
        )



    def get_lat_lng(self):
        return self.filter(
            lat__isnull=False,
            lng__isnull=False

        )


    def get_barcode(self):
        return self.filter(
            ~Q(barcode=''),
            barcode__isnull = False
        )

    def get_gt_depth(self):
        return self.filter(
            depth__gt = 100
        )

    def count_barcode(self):
        return self.get_barcode().count()
    

    


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

    objects = TrashCanQuerySet.as_manager()

    def has_address(self):
        return bool(self.address)
        #if self.address:
        #    return True
        #return False

    @property
    def tiene_address(self):
        return self.has_address()

    #def set_address(self):
        #if self.tiene_address:
            #return
        #self.address='Almacen Principal'

    #def save(self,*args, **kwargs):
        #self.set_address()
        #super(TrashCan, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'trash_can'



class LevelQuerySet(models.QuerySet):

    def get_levels(self, trash_can_pk):
        return self.filter(trash_can=trash_can_pk).order_by('-time')


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

    objects = LevelQuerySet.as_manager()

    
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


