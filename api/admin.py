from django.contrib import admin
from .models import MainData

@admin.register(MainData)
class AdminViewMainData(admin.ModelAdmin):
    list_display = ['id','fio','tg_id','tel_number','overall_sum']
    search_fields = ['tg_id','fio','tel_number']
    list_display_links = ['fio']
    list_per_page = 10
    ordering = ['id']