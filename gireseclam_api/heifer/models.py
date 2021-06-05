from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Beneficiaire(models.Model):
    name = models.CharField(max_length=200)
    sexe= models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    #post = models.ForeignKey('Post', models.DO_NOTHING, related_name='relateds')
    post = models.ForeignKey('Post', models.DO_NOTHING, related_name='post_ob')

    class Meta:
        managed = False
        db_table = 'comment'
#    def set_post_ob(self, post):
  #	    self.post =post
  
 #   def get_post_ob(self):
#  	    return self.post
#    def __str__(self):
  #      return self.content


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    '''
    def __init__(self, title, content,author ,*args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.title = title
        self.content = content
        self.author= author
    '''

    class Meta:
        managed = False
        db_table = 'post'
