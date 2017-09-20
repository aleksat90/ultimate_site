from django.forms import ModelForm
from blogapp import models


class PostForm(ModelForm):
    class Meta:
        fields = ('naslov', 'poruka')
        model = models.Post

