# Generated by Django 3.0.7 on 2021-03-09 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='active',
        ),
        migrations.AlterModelTable(
            name='category',
            table='tb_category',
        ),
        migrations.AlterModelTable(
            name='comment',
            table='tb_comment',
        ),
        migrations.AlterModelTable(
            name='post',
            table='tb_post',
        ),
    ]
