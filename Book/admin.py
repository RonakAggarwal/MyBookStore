from django.contrib import admin

# Register your models here.
from Book.models import Author,Category,Book

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
