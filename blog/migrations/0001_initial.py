# Generated by Django 3.0.7 on 2020-08-01 22:15

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', ckeditor.fields.RichTextField()),
                ('content', ckeditor.fields.RichTextField(verbose_name='content')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='uploads')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categoria.Category')),
            ],
        ),
    ]
