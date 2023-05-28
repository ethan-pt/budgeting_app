from django.db import models
from django.contrib.auth.models import User



class BudgetInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True, editable=True, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']