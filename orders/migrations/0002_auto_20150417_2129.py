# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField('Debil', 'last_name'),
        migrations.RenameField('Debil', 'first_name', 'name'),
    ]
