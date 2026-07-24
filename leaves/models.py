from django.db import models
from django.conf import settings


class Leave(models.Model):
    LEAVE_TYPE_CHOICES = (
        ('sick', 'Sick Leave'),
        ('casual', 'Casual Leave'),
        ('paid', 'Paid Leave'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='leaves')
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPE_CHOICES)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_on']

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type} ({self.status})"