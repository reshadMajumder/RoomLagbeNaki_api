from django.contrib import admin

# Register your models here.
from .models import Ad,AdImage

# Register your models here.


admin.site.register(Ad)
admin.site.register(AdImage)