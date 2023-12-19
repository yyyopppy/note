# from django.db import models
# # from django.contrib.auth.models import User
# from accounts.models import CustomUser
# from note.models import NotePost
# from django.conf import settings
# from datetime import datetime
# from django.utils import timezone


# class Reaction(models.Model):
#     REACTION_CHOICES = (
#         ('LIKE', 'Like'),
#         ('LOOK', 'Look'),
#         ('COMMENT', 'Comment'),
#     )

#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     note = models.ForeignKey(NotePost, on_delete=models.CASCADE)
#     reaction_type = models.CharField(max_length=10, choices=REACTION_CHOICES)
#     created_at = models.DateTimeField(default=datetime.now)
    
#     def __str__(self):
#         return f"{self.user.username} - {self.reaction_type}"
#     class Meta:
#         ordering = ['-created_at']

