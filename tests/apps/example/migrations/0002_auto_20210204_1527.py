# Generated by Django 3.1.5 on 2021-02-04 15:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=50, primary_key=True, serialize=False),
        ),
    ]
