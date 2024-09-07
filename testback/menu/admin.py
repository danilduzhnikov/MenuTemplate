from django.contrib import admin
from .models import MenuExample

class MenuExampleAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')  # Отображение в списке
    search_fields = ('name',)  # Поле поиска
    list_filter = ('parent',)  # Возможность фильтрации по родителю

admin.site.register(MenuExample, MenuExampleAdmin)