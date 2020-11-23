import django_filters
from .models import *
from django_filters import CharFilter
from django.contrib.auth.models import User

# Defines the filter to search username from User table
class UserFilter(django_filters.FilterSet):
    username = CharFilter(field_name='username', lookup_expr='icontains')

    class Meta:
        model = User
        fields = ('username',)

# Defines the filter to search location name from Entry table
class EntryFilter(django_filters.FilterSet):
    locations = CharFilter(field_name='Location_Name', lookup_expr='icontains')



    class Meta:
        model = Entry

        fields = ('locations',)
