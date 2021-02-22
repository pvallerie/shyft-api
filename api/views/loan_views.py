from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.loan import Loan
from ..serializers import LoanSerializer, UpdateLoanSerializer, CreateLoanSerializer

class Loans(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  serializer_class=LoanSerializer
  def get(self, request):
    """Index Request"""
    user_loans = Loan.objects.filter(bike_loaner=request.user.id)
    data = LoanSerializer(user_loans, many=True).data
    return Response(data)

  serializer_class = LoanSerializer
  def post(self, request):
    """Create loan"""
    request.data['loan']['bike_loaner'] = request.user.id
    loan = CreateLoanSerializer(data=request.data['loan'])
    if loan.is_valid():
      l = loan.save()
      return Response(loan.data, status=status.HTTP_201_CREATED)
    return Response(loan.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request, pk):
    """Show request"""
    loan = get_object_or_404(Loan, pk=pk)
    data = LoanSerializer(loan).data
    return Response({ 'loan': data })

  def delete(self, request, pk):
    """Delete Request"""
    loan = get_object_or_404(Loan, pk=pk)
    if not request.user.id == loan.bike_loaner.id:
      raise PermissionDenied('Unauthorized, you do not own this loan.')
    loan.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
    """Update request"""
    loan = get_object_or_404(Loan, pk=pk)
    if not request.user.id == loan.bike_loaner.id:
      raise PermissionDenied('Unauthorized, you do not own this loan.')
    request.data['loan']['bike_loaner'] = request.user.id
    data = UpdateLoanSerializer(loan, data=request.data['loan'], partial=True)
    if data.is_valid():
      data.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
