from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length = 30, unique = True)
#  description = models.TextField()

class Good(models.Model):
  name = models.CharField(max_length = 50, unique = True, verbose_name = "Название")
  description = models.TextField()
  in_stock = models.BooleanField(default = True, db_index = True, verbose_name = "В наличии")
  category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_NULL)

class BlogArticle(models.Model):
  title = models.CharField(unique_for_date = "pubdate")
  pubdate = models.DateField(auto_now_add = True)
  updated = models.DateField(auto_now = True)
