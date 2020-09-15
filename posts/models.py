from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

class Category(CommonInfo):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(CommonInfo):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='posts',on_delete=models.PROTECT)
    author = models.ForeignKey(User,related_name='posts',on_delete=models.PROTECT)
    content = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.author.get_full_name()}'
