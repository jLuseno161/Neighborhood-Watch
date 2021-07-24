from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=200)
    hood_location = models.CharField(max_length=200)
    hood_photo =CloudinaryField('photo', default='photo')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return f'{self.hood_name} neighbourhood'

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()
        
    @classmethod
    def find_hood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    @property
    def occupants_count(self):
        return self.neighbourhood_users.count()

    def update_hood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name

          

# class User(AbstractUser):
#     neighbourhood = models.ForeignKey(
#         Neighbourhood, on_delete=models.CASCADE, related_name='neighbourhood_users', blank=True, null=True)
    
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default='0')
#     neighbourhood_id = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='members', blank=True, null=True)
#     neighbourhood_name = models.CharField(max_length=60,blank=False)
#     location = models.CharField(max_length=60,blank=False)
#     bio = models.TextField()
