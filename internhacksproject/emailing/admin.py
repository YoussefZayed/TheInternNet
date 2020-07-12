from django.contrib import admin

from .models import EmailSent, Template

admin.site.register(EmailSent)
admin.site.register(Template)