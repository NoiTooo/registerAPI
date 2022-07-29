from ast import Or
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, OrganizationSerializer
from .models import Organization

User = get_user_model()


class RelationshipAPI(generics.ListAPIView):
    """ follows&followees / required jwtToken"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ followees """
        my_followees = User.objects.filter(follows=request.user)
        followees_count = len(my_followees)
        followees = []
        for fwees in range(followees_count):
            followees.append(str(my_followees[fwees].id))

        """ follows """
        user = User.objects.get(id=request.user.id)
        follows_count = len(user.follows.all())
        follows = []
        my_follows = user.follows.all()
        for fws in range(followees_count):
            follows.append(str(my_follows[fws].id))

        data = {
            'followees_count': followees_count,
            'followees': followees,
            'follows_count': follows_count,
            'follows': follows
        }
        return JsonResponse(data=data)


class OrganizationAPI(generics.ListAPIView):
    """ orgnization / required jwtToken"""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        li = user.organizations_users.all()
        affiliation = []
        for i in range(len(li)):
            affiliation.append(li[i].name)

        data = {
            'organization': affiliation
        }
        return JsonResponse(data=data)
