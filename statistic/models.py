from django.db import models


class StaticItem(models.Model):
    date = models.DateField()
    views = models.IntegerField(blank=True, null=True)
    click = models.IntegerField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = verbose_name
        ordering = ('-date',)
