from django.db import models

# Create your models here.

from django.db.models import CharField, TextField, DateTimeField, ImageField, ForeignKey


class Post(models.Model):
    title = CharField(max_length=100)
    text = TextField()
    image = ImageField(upload_to="images/%Y/%m/%d")
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = TextField()
    post = ForeignKey(Post, on_delete=models.CASCADE)
    email = CharField(max_length=100)
    created_at = DateTimeField(auto_now_add=True)
    updated_ad = DateTimeField(auto_now=True)

    def __str__(self):
        return self.email