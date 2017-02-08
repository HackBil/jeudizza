from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Company, Debil, Order, Dept


INVITED_PREFIX = "Invité(e) de"


@receiver(post_save, sender=Company)
def create_invited_debil(sender, instance, created, **kwargs):
    if created:
        Debil(name="%s %s" % (INVITED_PREFIX, instance.name), company=instance).save()


@receiver(post_save, sender=Order)
def create_depts(sender, instance, created, **kwargs):
    if not instance.open:  # We closed the order
        for pizzaOrder in instance.pizzaorder_set.all():
            Dept(debil=pizzaOrder.debil, amount=pizzaOrder.get_price()).save()
