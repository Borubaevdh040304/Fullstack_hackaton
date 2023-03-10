from django.db import models
from django.contrib.auth import get_user_model

from main.models import Post, Restaurant

User = get_user_model()


class RestourantComments(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='restcomments', on_delete=models.CASCADE)
    pestouran = models.ForeignKey(Restaurant, related_name='restcomments', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} -> {self.pestouran}'


class PostComments(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='postcomments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='postcomments', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} -> {self.post}'


class RestourantFavorites(models.Model):
    user = models.ForeignKey(User, related_name='pestourant_favorite' , on_delete=models.CASCADE)
    restourant = models.ForeignKey(Restaurant, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} -> {self.restourant}'


class PostFavorites(models.Model):
    user = models.ForeignKey(User, related_name='post_favorites' , on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}-> {self.post}'


class RatingRestourant(models.Model):
    lesson = models.ForeignKey(Restaurant, related_name='ratings', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])


    def __str__(self):
        return f'{self.author} -> {self.lesson}'
        

class PostLike(models.Model):
    user = models.ForeignKey(User, related_name='post_likes' , on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)


# class Rec(models.Model):
#     rec = models.ForeignKey(RatingRestourant, related_name='rec', on_delete=models.CASCADE, default='')
     