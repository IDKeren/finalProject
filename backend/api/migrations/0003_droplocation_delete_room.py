# Generated by Django 5.1 on 2024-08-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_room_delete_datamodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DropLocation',
            fields=[
                ('drop_id', models.AutoField(primary_key=True, serialize=False)),
                ('drop_x_coordinate', models.FloatField()),
                ('drop_y_coordinate', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
