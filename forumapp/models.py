from django.contrib.auth.models import User
from django.db import models

from django.utils import timezone


class ForumSection(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Forum(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(max_length=200)
    section = models.ForeignKey(
        ForumSection,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=100)
    forum = models.ForeignKey(Forum, null=True, on_delete=models.CASCADE)
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('can_remove_any_thread', 'Can remove ANY thread.'),
            ('can_pin_threads', 'Can pin threads.')
        ]
        ordering = [
            'pinned'
        ]


class ThreadResponse(models.Model):
    thread = models.ForeignKey(Thread, null=True, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(null=True)
    responder = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    edited = models.BooleanField(default=False)
    order_in_thread = models.PositiveIntegerField(default=1)

    class Meta:
        permissions = [('can_remove_any_response', 'Can remove ANY response.')]
        ordering = ['created_datetime']

    def __str__(self):
        return self.message


class LikeDislike(models.Model):

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    like = models.BooleanField(default=True)
    response = models.ForeignKey(
        ThreadResponse,
        null=False,
        on_delete=models.CASCADE
    )


class ForumUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    banned_until = models.DateTimeField(default=timezone.now)

    class Meta:
        permissions = [
            ('can_ban_users', 'Can ban any user.')
        ]
