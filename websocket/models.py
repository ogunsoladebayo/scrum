from django.db import connection, models

# Create your models here.

class Connection(models.Model):
    connection_id = models.CharField(max_length=255)

    def __str__(self):
        return self.connection_id


class ChatMessage(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    timestamp = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    def as_dict(self):
        return {
            "username": self.username,
            "message": self.message,
            "timestamp": self.timestamp
        }
