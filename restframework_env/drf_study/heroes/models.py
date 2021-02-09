from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Hero(models.Model):
    ATRIBUTE_TYPES = (
        (1, 'Streng'),
        (2, 'Agility'),
        (3, 'Intelligence')
    )

    name = models.CharField(verbose_name='Name of hero',  
                            db_index=True,
                            unique=True,
                            max_length=100)
    hp = models.IntegerField(verbose_name='Health oint')
    mana = models.IntegerField(verbose_name='Health oint')
    fraction = models.CharField(verbose_name='Fraction',
                                max_length=100)
    atribute = models.IntegerField(verbose_name='Atribute',
                                    choices=ATRIBUTE_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)