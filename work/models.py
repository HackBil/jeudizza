from django.db import models
from orders.models import Debil
from random import shuffle


# def weighted_shuffle(a, w):
#     w = list(w)  # make a copy of w
#     if len(a) != len(w):
#         print("weighted_shuffle: Lenghts of lists don't match.")
#         return

#     r = [0] * len(a)  # contains the random shuffle
#     for i in range(len(a)):
#         j = weighted_choice(w)
#         r[i] = a[j]
#         w[j] = 0
#     return r


class Chore(models.Model):
    name = models.CharField(max_length=256, unique=True)
    chorables = models.ManyToManyField(Debil, through='ChoreDebil', related_name='chorables_set')
    last_debil = models.ForeignKey(Debil, null=True, blank=True, related_name='last_chores_set')
    last_execution = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def pick_random_debil(self):
        return shuffle(list(self.chorables.all()))[0]


class ChoreDebil(models.Model):
    chore = models.ForeignKey(Chore)
    debil = models.ForeignKey(Debil, verbose_name='déBIL')
    last_chore = models.DateField(null=True, blank=True)
    weight = models.IntegerField(default=5)
