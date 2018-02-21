from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length = 30, unique = True)
#  description = models.TextField()

  def __str__(self):
    return self.name

class Good(models.Model):

  class Meta:
    ordering = ["-price", "name"]
    unique_together = ("category", "name", "price")
    verbose_name = "товар"
    verbose_name_plural = "товары"

  name = models.CharField(max_length = 50, unique = True, verbose_name = "Название")
  description = models.TextField()
  in_stock = models.BooleanField(default = True, db_index = True, verbose_name = "В наличии")
  category = models.ForeignKey(Category, null = True, blank = True, on_delete = models.SET_NULL)
  price = models.FloatField()

  def __str__(self):
    s = self.name
    if not self.in_stock:
      s = s + " (нет в наличии)"
    return s

  def save(self, *args, **kwargs):
    # Выполненяем дополнительные действия перед сохранением записи

    # Обязательно вызываем метод save родителя,
    # который, собственно, выполняет сохранение записи.
    # Если мы этого не сделаем, запись не будет сохранена
    super(Good, self).save(*args, **kwargs)

    # Выполняем какие-либо действия после сохранения записи

  def delete(self, *args, **kwargs):
    # Выполняем дополнительные действия перед удалением записи

    # Обязательно вызываем метод delete родителя,
    # иначе запись не будет удалена
    super(Good, self).delete(*args, **kwargs)

    # Выполняем какие-либо действия после удаления записи

  def get_is_stock(self):
    if self.in_stock:
      return "+"
    else:
      return ""

class BlogArticle(models.Model):
  title = models.CharField(max_length = 50, unique_for_date = "pubdate")
  pubdate = models.DateField(auto_now_add = True)
  updated = models.DateField(auto_now = True)
