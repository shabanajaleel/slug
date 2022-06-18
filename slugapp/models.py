from django.db import models
from django.utils.text import slugify

# Create your models here.
class Article(models.Model):
    Name=models.CharField(max_length=40,unique=True)
    Author=models.CharField(max_length=20)
    Description=models.TextField()
    article_slug=models.SlugField(max_length=20,null=True,blank=True)

    class Meta:
        db_table="Article"
        ordering=['id']

    def save(self, *args, **kwargs):
        self.article_slug = slugify(self.Name)
        super(Article, self).save(*args, **kwargs)  
