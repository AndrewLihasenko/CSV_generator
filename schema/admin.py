from django.contrib import admin
from .models import NewSchema, SchemaColumn


admin.site.register(NewSchema)
# admin.site.register(SchemaColumn)


@admin.register(SchemaColumn)
class SchemaColumnAdmin(admin.ModelAdmin):
    # list_display = ('column_name', 'drop_down_list')
    fields = [('column_name', 'drop_down_list')]
