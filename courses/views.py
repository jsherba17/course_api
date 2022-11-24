from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Courses, Branches, Contacts
from .serializers import CoursesSerializer, BranchesSerializer, ContactsSerializer

class CoursesAPIView(APIView):

    def get(self,request):
        c = Courses.objects.all()
        return Response({'posts': CoursesSerializer(c, many=True).data})

    def post(self,request):
        serializer = CoursesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response ({'posts': serializer.data})


class BranchesAPIView(APIView) :

    def get(self, request) :
        b = Branches.objects.all()
        return Response({'posts' : BranchesSerializer(b, many=True).data})

    def post(self, request) :
        serializer = BranchesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'posts' : serializer.data})


class ContactsAPIView(APIView) :

    def get(self, request) :
        a = Contacts.objects.all()
        return Response({'creat' : ContactsSerializer(a, many=True).data})

    def post(self, request) :
        serializer = ContactsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'creat' : serializer.data})
