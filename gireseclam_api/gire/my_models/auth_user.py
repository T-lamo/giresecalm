from django.db import models

class AuthUser(models.Model):
    fonction_detail=""
    ong_detail=""
    fonction = models.ForeignKey('FonctionTb', models.DO_NOTHING, blank=True, null=True,related_name='users')
    ong = models.ForeignKey('OngTb', models.DO_NOTHING, blank=True, null=True, related_name='users')
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    telephone = models.TextField(blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()


    def set_fonction_detail(self, f):
  	    self.fonction_detail =f
  
    def get_fonction_detail(self):
  	    return self.fonction_detail

    def set_ong_detail(self,o):
         self.ong_detail=o
    def get_ong_detail(self):
  	    return self.ong_detail

    class Meta:
        managed = False
        db_table = 'auth_user'