# Generated by Django 4.2.6 on 2023-10-25 12:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.EmailField(blank=True, max_length=150, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
