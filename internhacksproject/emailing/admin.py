from django.contrib import admin

from .models import Contact, Email

admin.site.register(Contact)
admin.site.register(Email)