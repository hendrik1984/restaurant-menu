from django.contrib import admin
from django.utils.html import format_html
from .models import Category, MenuItem
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ("name", "description")
  search_fields = ("name",)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
  list_display = ("thumbnail", "name", "category", "price", "is_available")
  list_filter = ("category", "is_available")
  search_fields = ("name", "description")
  readonly_fields = ("image_preview",)

  fieldsets = (
     ("Image", {
        "fields": ("image_preview", "image"),
     }),
     ("Details", {
        "fields": ("name", "description", "price", "category", "is_available"),
     })
  )

  @admin.display(description="Image")
  def thumbnail(self, obj):
    if obj.image:
        return format_html(
            '<img src="{}" style="height:50px;width:50px;'
            'object-fit:cover;border-radius:6px;" />',
            obj.image.url,
        )
    return "—"

  @admin.display(description="Current image")
  def image_preview(self, obj):
    if obj.image:
        return format_html(
            '<img src="{}" style="max-height:200px;'
            'border-radius:8px;box-shadow:0 2px 6px rgba(0,0,0,0.1);" />',
            obj.image.url,
        )
    return "No image uploaded yet."