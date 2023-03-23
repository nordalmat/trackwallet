from django.db import models


class Currency(models.Model):
    ticker = models.CharField(max_length=3, default=None, blank=True, null=True)
    name = models.CharField(max_length=50, default=None, blank=True, null=True)

    def __str__(self):
        return self.ticker

    class Meta:
        verbose_name_plural = 'Currencies'
        ordering = ['ticker']

    