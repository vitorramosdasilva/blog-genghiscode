from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.html import mark_safe
from django.urls import reverse


class Category(models.Model):
    nome = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    content = RichTextField(verbose_name="content")
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    imagem = models.ImageField(upload_to="uploads", blank=True, null=True)

    def get_absolute_url_update(self):
        return reverse('post_edit', args=[self.pk])

    @property
    def view_image(self):
        return mark_safe('<img src="%s" width="400px" />' % self.imagem.url)
        view_image.short_description = "Imagem Cadastrada"
        view_image.allow_tags = True

    def __str__(self):
        return self.title


