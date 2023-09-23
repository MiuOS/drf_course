from django.contrib import admin
<<<<<<< HEAD
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'email')
=======

# Register your models here.
>>>>>>> 1dfba54f1272c1f92fa2949c1038b6845b34ac7e
