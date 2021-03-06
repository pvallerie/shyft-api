from django.urls import path
from .views.bike_views import Bikes, BikeDetail
from .views.loan_views import Loans, LoanDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('bikes', Bikes.as_view(), name='bikes'),
    path('bikes/<int:pk>', BikeDetail.as_view(), name='bike_detail'),
    path('loans', Loans.as_view(), name='loans'),
    path('loans/<int:pk>', LoanDetail.as_view(), name='loan_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
