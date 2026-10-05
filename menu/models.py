from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True)

  class Meta:
    verbose_name_plural = "categories"

  def __str__(self):
    return self.name

class MenuItem(models.Model):
  name = models.CharField(max_length=150)
  description = models.TextField(blank=True)
  price = models.DecimalField(max_digits=8, decimal_places=2)
  category = models.ForeignKey(
    Category,
    related_name="items",
    on_delete=models.CASCADE,
  )
  is_available = models.BooleanField(default=True)
  image = models.ImageField(
    upload_to="menu_items/",
    blank=True,
    null=True,
  )

  def __str__(self):
    return self.name