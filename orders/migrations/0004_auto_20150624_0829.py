# -*- coding: utf-8 -*-


from django.db import models, migrations

INVITED_PREFIX = "Invité(e) de"


def create_invited_people(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Debil = apps.get_model("orders", "Debil")
    Company = apps.get_model("orders", "Company")
    for company in Company.objects.all():
        Debil(name="%s %s" % (INVITED_PREFIX, company.name), company=company).save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20150417_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='debil',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='pizza',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='pizzaorder',
            name='crust',
            field=models.ForeignKey(verbose_name='p\xe2te', to='orders.Crust'),
        ),
        migrations.RunPython(create_invited_people),
    ]
