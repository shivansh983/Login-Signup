from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group , Permission


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add related_name to avoid clashes with the default User model
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

class FriendRequest(models.Model):
    """
    Model to represent friend requests between users.
    """
    # Sender of the friend request
    from_user = models.ForeignKey(CustomUser, related_name='sent_requests', on_delete=models.CASCADE)
    
    # Receiver of the friend request
    to_user = models.ForeignKey(CustomUser, related_name='received_requests', on_delete=models.CASCADE)
    
    # Status of the friend request
    STATUS_CHOICES = [
        ('pending', 'Pending'), 
        ('accepted', 'Accepted'), 
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    # Timestamp when the friend request was created
    created_at = models.DateTimeField(auto_now_add=True)

    def accept(self):
        """
        Accept the friend request.
        """
        self.status = 'accepted'
        self.save()

    def reject(self):
        """
        Reject the friend request.
        """
        self.status = 'rejected'
        self.save()

    @property
    def is_pending(self):
        """
        Check if the friend request is pending.
        """
        return self.status == 'pending'

    def __str__(self):
        """
        String representation of the friend request.
        """
        return f"FriendRequest from {self.from_user} to {self.to_user}, Status: {self.status}"
