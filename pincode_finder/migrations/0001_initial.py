# Generated by Django 5.1.3 on 2024-11-30 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('pincode', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
            ],
        ),
    ]