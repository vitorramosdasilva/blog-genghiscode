# from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Category(models.Model):
    nome = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "tb_category"

    def __str__(self):
        return self.nome


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    imagem = CloudinaryField('imagem')
    # summary = RichTextField()
    # content = RichTextField(verbose_name="content")

    class Meta:
        db_table = "tb_post"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # returns us to the post-detail view. can also set this to blog-home
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    texto = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "tb_comment"

    def approve(self):
        self.active = True
        self.save()

    def __str__(self):
        return self.texto