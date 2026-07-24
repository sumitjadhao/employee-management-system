from django.db import models
from django.conf import settings


class Payroll(models.Model):
    MONTH_CHOICES = (
        (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'),
        (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'),
        (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December'),
    )

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payrolls')
    month = models.IntegerField(choices=MONTH_CHOICES)
    year = models.IntegerField()
    basic_pay = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    generated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('employee', 'month', 'year')
        ordering = ['-year', '-month']

    def save(self, *args, **kwargs):
        self.net_pay = self.basic_pay + self.allowances - self.deductions
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee.username} - {self.get_month_display()} {self.year}"