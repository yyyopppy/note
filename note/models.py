from django.db import models
from accounts.models import CustomUser
from django.urls import reverse #commetで追加
#from django.contrib.auth.models import CustomUser
# from reactions.models import Reaction


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20
    )

    def __str__(self):
        return self.title
    

class NotePost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
    )

    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
    )

    comment = models.TextField(
        verbose_name='コメント',
    )

    image1 = models.ImageField(
        verbose_name='イメージ1',
        upload_to='notes',
        blank=True,
        null=True
    )

    image2 = models.ImageField(
        verbose_name='イメージ2',
        upload_to='notes',
        blank=True,
        null=True
    )

    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )

    likes = models.ManyToManyField(CustomUser, related_name='notepost_like',  blank=True)
    def number_of_likes(self):
        return self.likes.count()


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.title
    



class Comment(models.Model):
    post = models.ForeignKey(NotePost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text[:50] 
    


class Like(models.Model):
    # いいねに関するフィールド
    post = models.ForeignKey(NotePost, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    


# class Reaction(models.Model):
#      OK = 'OK'
#      COMMENT = 'COMMENT'

#      REACTION_CHOICES = [
#          (OK, '見ました'),
#          (COMMENT, 'コメントあり'),
#      ]
#     reactions = models.ForeignKey('reaction.Reaction', on_delete=models.CASCADE)
#      user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     note = models.ForeignKey(NotePost, on_delete=models.CASCADE)
#      reaction_type = models.CharField(max_length=20, choices=REACTION_CHOICES)

#      def __str__(self):
#          return f"{self.user.username} reacted {self.reaction_type} to {self.note.title}"
