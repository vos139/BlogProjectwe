from django.db import models
from django.utils import timezone
#from myproject import settings
from django.conf import settings

#class for consultant to add/edit post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#class for consultant to reply on posts
class Post_Reply(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    published_date = models.DateTimeField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text




#class for learner to add/edit post

class Lear_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



#class for learner to add reply

class Learn_Reply(models.Model):
    post = models.ForeignKey('blog.Lear_Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    published_date = models.DateTimeField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
