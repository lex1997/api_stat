from django.db import models


class Case(models.Model):
    date = models.DateField(verbose_name="Дата события")
    views = models.IntegerField("Количество показов", blank=True, null=True)
    clics = models.IntegerField("Количество кликов", blank=True, null=True)
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Стоимость клика",
        blank=True,
        null=True,
    )



    class Meta:
        ordering = ("date",)
