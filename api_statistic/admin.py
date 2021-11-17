from django.contrib import admin
from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ('date', 'views', 'clics', 'cost')
    list_display_links = ('date', 'views', 'clics', 'cost')
    search_fields = ('date', 'views', 'clics', 'cost')
    list_editable = ('done',)
    list_filter = ('done',)

admin.site.register(Case)

