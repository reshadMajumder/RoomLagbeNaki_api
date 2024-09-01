from django.contrib import admin

# Register your models here.
from .models import Ad,AdImage,Banner

# Register your models here.


admin.site.register(Ad)
admin.site.register(AdImage)



@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt_text', 'image')
    search_fields = ('alt_text',)
