from django_cron import CronJobBase, Schedule
from orders.models import Order
import datetime


def next_thursday():
    d = datetime.datetime.now()
    days_ahead = 3 - d.weekday()  # 3=thursday
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


class Jeudi(CronJobBase):
    RUN_EVERY_MINS = 120

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'orders.jeudi'    # a unique code

    def do(self):
        last_order = Order.objects.all().order_by('pk').last()
        last_order.open = False
        last_order.save()

        o = Order(date=next_thursday())
        o.save()
