from django.contrib import admin

# Register your models here.

from myapp.models import Passanger, Vehicle, Book

admin.site.register(Passanger)
admin.site.register(Vehicle)
admin.site.register(Book)