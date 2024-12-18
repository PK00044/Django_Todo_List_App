from django.db import models


class ToDo(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)  # Auto-set on creation
    title = models.CharField(max_length=100)  # Mandatory
    description = models.TextField(max_length=1000)  # Mandatory
    due_date = models.DateField(null=True, blank=True)  # Optional
    tags = models.TextField(null=True, blank=True)  # Optional, comma-separated
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')  # Mandatory

    def __str__(self):
        return self.title
