# Generated by Django 4.1.4 on 2023-03-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_full_name_alter_empleado_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
