from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MainMenu(models.Model):
    item = models.CharField(max_length=200, unique=True)
    link = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.item


class Book(models.Model):
    name = models.CharField(max_length=200)
    web = models.URLField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    publishdate = models.DateField(auto_now=True)
    picture = models.FileField(upload_to='bookEx/static/uploads')
    pic_path = models.CharField(max_length=300, editable=False, blank=True)
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    # adding a favorite attribute for the Favorites Page
    favorite = models.BooleanField(default=False, null=True)
    # add rate field
    rated = models.IntegerField(null=True)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    up_votes = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['up_votes']

    def __str__(self):
        return 'Comment by {} at {}'.format(self.username, self.created_on)
