from django.db import models

class MenuExample(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories', verbose_name='Родительская категория')

    class Meta:
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

    def __str__(self):
        return self.name