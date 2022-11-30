from django.db import models

# Create your models here.


class Comment(models.Model):
    author = models.CharField(max_length=150)
    comment_body = models.TextField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True)
    sentiment_score = models.DecimalField(max_digits=5, decimal_places=4)

    def is_negative(self):
        return True if self.sentiment_score < 0 else False

    def __str__(self):
        return self.comment_body
