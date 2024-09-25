from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    TRANSACTION_CATEGORIES = [
        ('general', 'General'),
        ('groceries', 'Groceries'),
        ('shopping', 'Shopping'),
        ('restaurant', 'Restaurant'),
        ('transport', 'Transport'),
        ('travel', 'Travel'),
        ('entertainment', 'Entertainment'),
        ('utilities', 'Utilities'),
        ('health', 'Health'),
        ('services', 'Services'),
        ('charity', 'Charity'),
    ]
    

    transaction_date = models.DateField()
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=TRANSACTION_CATEGORIES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - {self.amount}"
