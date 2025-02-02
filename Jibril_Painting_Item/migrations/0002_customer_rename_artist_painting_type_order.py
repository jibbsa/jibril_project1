# Generated by Django 5.0.2 on 2024-03-22 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jibril_Painting_Item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='painting',
            old_name='artist',
            new_name='type',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('painting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='Jibril_Painting_Item.painting')),
            ],
        ),
    ]
