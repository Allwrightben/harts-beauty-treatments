from django.contrib import admin
from .models import Treatment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Treatment)
class TreatmentAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
