from django.contrib import admin
from django.utils.html import format_html, format_html_join
from django.utils.safestring import mark_safe

from .models import NewSchema, SchemaColumn


admin.site.register(NewSchema)
# admin.site.register(SchemaColumn)


@admin.register(SchemaColumn)
class SchemaColumnAdmin(admin.ModelAdmin):
    # list_display = ('column_name', 'drop_down_list')
    # fields = [('column_name', 'drop_down_list')]

    readonly_fields = ('drop_down_list',)
    fieldsets = (
        ('Основная информация', {
            'fields': [('column_name', 'drop_down_list',)],
        }),
    )

    def drop_down_list(self, instance):
        return format_html(
            # mark_safe('<br>'),
            # '{}',
            # '<select>{} {}</select>',
            # mark_safe('<select>{}</select>'),
            '<select></select>',
            # self.address,
            # self.date,
        )

    drop_down_list.short_description = "Type"
