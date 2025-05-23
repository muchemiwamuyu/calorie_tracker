# Generated by Django 5.2.1 on 2025-05-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isVegetarian', models.BooleanField(default=False)),
                ('water', models.FloatField()),
                ('food_item', models.CharField(choices=[('fruit', 'Fruit'), ('vegetable', 'Vegetable'), ('grain', 'Grain'), ('protein', 'Protein'), ('dairy', 'Dairy')], max_length=50)),
            ],
        ),
    ]
