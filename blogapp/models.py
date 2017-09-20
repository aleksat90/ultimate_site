
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    autor = models.ForeignKey(User, blank= True, null= True)
    poruka = models.TextField()
    datum_kreiranja = models.DateTimeField(auto_now = True)
    naslov = models.CharField(max_length = 100)

    def get_absolute_url(self):
        print("u metodi sam")
        print(self.pk)
        return reverse('blogapp:post_pojedinacan', kwargs={'pk': self.pk})

    def __str__(self):
        return self.naslov
