from django.contrib import admin

from .models import Classify, BillInfo
# Register your models here.


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('name')
admin.site.register(Classify)

class BillInfoAdmin(admin.ModelAdmin):
    list_display = ('type', 'classify', 'date', 'money', 'ps')
admin.site.register(BillInfo)

