from django.db import models

# Create your models here.
class Bills(models.Model):
    # billing and payments page
    # making changes to this page requires migrations to the database!
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    ispaid = models.BooleanField(default=False)
    date_due = models.DateField()
    bills_total = models.Sum()

    def __str__(self):
        ## dunder str method (double underscore)
        ## these are known as "magic methods"

        #cast the decimal value to a string to return
        return self.title