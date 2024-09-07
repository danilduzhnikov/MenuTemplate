from django import template
from menu.models import *

register = template.Library()

@register.simple_tag()
def get_menu():
    # Получаем все категории
    all_categories = MenuExample.objects.all()

    # Создаем словарь для хранения родительских категорий и их подкатегорий
    menu_dict = {}

    # Проходим по всем категориям и разделяем их на родительские и подкатегории
    for category in all_categories:
        if category.parent_id is None:
            # Если категория родительская, добавляем ее в словарь
            menu_dict[category] = []

    # Проходим по всем категориям снова для добавления подкатегорий
    for category in all_categories:
        if category.parent_id is not None:
            parent_category = MenuExample.objects.filter(id=category.parent_id).first()
            if parent_category in menu_dict:
                menu_dict[parent_category].append(category)

    return menu_dict