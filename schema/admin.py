from django.contrib import admin
from .models import NewSchema, SchemaColumn


# admin.site.register(NewSchema)
# admin.site.register(SchemaColumns)

@admin.register(SchemaColumn)
class SchemaColumnAdmin(admin.ModelAdmin):
    fields = [('column_name', 'type')]
