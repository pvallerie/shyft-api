from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.bike import Bike
from ..serializers import BikeSerializer, UpdateBikeSerializer

class Bikes(generics.ListCreateAPIView):
  permission_classes=(IsAuthenticated,)
  serializer_class=BikeSerializer
  def get(self, request):
    """Index Request"""
    bikes = Bike.objects.all()
    data = BikeSerializer(bikes, many=True).data
    return Response({ 'bikes': data })

  def post(self, request):
    """Create request"""
    request.data['bike']['owner'] = request.user.id
    bike = BikeSerializer(data=request.data['bike'])
    if bike.is_valid():
      bike.save()
      return Response({ 'bike': bike.data }, status=status.HTTP_201_CREATED)
    return Response(bike.errors, status=status.HTTP_400_BAD_REQUEST)

class BikeDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes=(IsAuthenticated,)
  def get(self, request, pk):
    """Show request"""
    bike = get_object_or_404(Bike, pk=pk)
    data = BikeSerializer(bike).data
    return Response({ 'bike': data })

  def delete(self, request, pk):
    """Delete request"""
    bike = get_object_or_404(Bike, pk=pk)
    if not request.user.id == bike.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this bike.')
    bike.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def partial_update(self, request, pk):
    """Update reqeust"""
    bike = get_object_or_404(Bike, pk=pk)
    if not request.user.id == bike.owner.id:
      raise PermissionDenied('Unauthorized, you do not own this bike.')
    request.data['bike']['owner'] = request.user.id
    data = UpdateBikeSerializer(bike, data=request.data['bike'], partial=True)
    if data.is_valid():
      data.save()
      return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
