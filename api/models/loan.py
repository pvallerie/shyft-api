from django.db import models
from django.contrib.auth import get_user_model

class Loan(models.Model):
  pickup_date = models.DateField(auto_now=False, auto_now_add=False)
  dropoff_date = models.DateField(auto_now=False, auto_now_add=False)
  bike = models.ForeignKey('Bike', on_delete=models.CASCADE)
  bike_loaner = models.ForeignKey(
    get_user_model(),
    related_name='loans',
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"Loan for '{self.bike}' is due on '{self.dropoff_date}'"

  def as_dict(self):
    return {
      'id': self.id,
      'pickup_date': self.pickup_date,
      'dropoff_date': self.dropoff_date,
      'bike': self.bike,
      'bike_loaner': self.bike_loaner
    }
