from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


# This registers the About model with the Django admin site .
# The SummernoteModelAdmin allows for rich text editing.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'updated_on')
    summernote_fields = ('professional', 'personal')
