from django_cron import CronJobBase, Schedule
from oders.models import Order
import datetime


JEUDI = 3


def next_weekday(weekday):
    d = datetime.now()
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)


class Jeudi(CronJobBase):
    RUN_AT_TIMES = ['23:55']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'orders.jeudi'    # a unique code

    def do(self):
        last_order = Order.objects.all().order_by('pk').last()
        last_order.open = False
        last_order.save()

        Order(date=next_weekday(JEUDI)).save()
