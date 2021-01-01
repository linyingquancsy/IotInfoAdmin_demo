from django.contrib import admin
from login import models

# Register your models here.

admin.site.register(models.User)
admin.site.register(models.ConfirmString)
