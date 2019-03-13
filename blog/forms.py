from django import forms
#from .decorators import consultant_required, learner_required
from .models import Post, Lear_Post, Post_Reply, Learn_Reply

#Consultant form to add/edit post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

#Learner form to add/edit post
class LearnPostForm(forms.ModelForm):
    class Meta:
        model = Lear_Post
        fields = ('title', 'text',)
#Consultant form for reply
class Reply_Form(forms.ModelForm):
    class Meta:
        model = Post_Reply
        fields = ('text',)
#learner form for reply
class Learn_Form(forms.ModelForm):
    class Meta:
        model = Learn_Reply
        fields = ('text',)
