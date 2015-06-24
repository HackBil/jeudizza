# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Company, Debil


INVITED_PREFIX = u"Invité(e) de"


@receiver(post_save, sender=Company)
def create_invited_debil(sender, instance, created, **kwargs):
    if created:
        Debil(name=u"%s %s" % (INVITED_PREFIX, instance.name), company=instance).save()
