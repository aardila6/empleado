# Generated by Django 4.1.4 on 2023-01-09 14:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='texto'),
            preserve_default=False,
        ),
    ]
