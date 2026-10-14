from django.db import models


class StudentFeedback(models.Model):

    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    student_name = models.CharField(max_length=100)

    roll_number = models.CharField(max_length=50)

    subject = models.CharField(max_length=100)

    rating = models.IntegerField(
        choices=RATING_CHOICES
    )

    comments = models.TextField()

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.student_name