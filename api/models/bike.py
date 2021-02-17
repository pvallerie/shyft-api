from django.db import models
from django.contrib.auth import get_user_model
# from multiselectfield import MultiSelectField
#
# MY_TYPE_CHOICES = (('Mountain', 'Mountain'),
#                    ('Road', 'Road'),
#                    ('Trail', 'Trail'))
#
# MY_SIZE_CHOICES = (('S', 'Small'),
#                    ('M', 'Medium'),
#                    ('L', 'Large'))

class Bike(models.Model):
  name = models.CharField(max_length=100)
  # type = MultiSelectField(choices=MY_TYPE_CHOICES)
  # size = MultiSelectField(choices=MY_SIZE_CHOICES)
  type = models.CharField(max_length=20)
  size = models.CharField(max_length=20)
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
      'type': self.type,
      'size': self.size,
      'location': self.location,
      'owner': self.owner
      }
