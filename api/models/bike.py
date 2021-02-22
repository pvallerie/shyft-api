from django.db import models
from django.contrib.auth import get_user_model

class Bike(models.Model):
  name = models.CharField(max_length=100)
  image = models.CharField(max_length=300)
  type = models.CharField(max_length=20)
  size = models.CharField(max_length=20)
  rate = models.DecimalField(max_digits=6, decimal_places=2)
  location = models.CharField(max_length=100)
  owner = models.ForeignKey(
    get_user_model(),
    related_name='bikes',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"'{self.name}' belongs to '{self.owner}'"

  def as_dict(self):
    """Returns dictionary version of Bike"""
    return {
      'id': self.id,
      'name': self.name,
      'image': self.image,
      'type': self.type,
      'size': self.size,
      'location': self.location,
      'owner': self.owner
      }
