from django.contrib import admin
from .models import Artical

# Register your models here.
#admin.site.register(Artical)
@admin.register(Artical)

class ArticalModel(admin.ModelAdmin):
 list_filter = ('title', 'description')
 list_display = ('title', 'description')
 