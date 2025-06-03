from django.db import models
from django.utils import timezone
from django.conf import settings



# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def publish(self):
            self.created_at = timezone.now()
            self.save() 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Newest posts first
 

