from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Courses, Branches, Contacts


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ['latitude', 'longitude', 'address']

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['type', 'value']

class CoursesSerializer(serializers.ModelSerializer):
    branches = BranchesSerializer(many=True)
    contacts = ContactsSerializer(many=True)
    class Meta:
        model = Courses
        fields = ['id','name', 'description', 'logo', 'branches','contacts']

    def create(self, validated_data):
            branches_data = validated_data.pop('branches')
            contacts_data = validated_data.pop('contacts')

            course = Courses.objects.create(**validated_data)
            for branch_data in branches_data:
                Branches.objects.create(course=course, **branch_data)
            for contact_data in contacts_data:
                Contacts.objects.create(course=course, **contact_data)
            return course
