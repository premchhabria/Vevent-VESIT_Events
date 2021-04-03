from django.contrib import admin

# Register your models here.
from .models import Events

admin.site.register(Events)
admin.site.site_header = "VESIT Events"