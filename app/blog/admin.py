from django.contrib import admin

from blog import models


admin.site.register(models.Entry)
admin.site.register(models.Category)
