from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class BudgetInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.00)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100)
    amount = models.FloatField(default=0.00)
    date = models.DateField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']