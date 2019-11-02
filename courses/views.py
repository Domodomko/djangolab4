from courses.models import Course
from courses.serializers import CourseSerializer, CategorySerializer, ContactSerializer, BranchSerializer
from rest_framework import generics, viewsets

class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

class CourseCreateView(generics.CreateAPIView):
    model = Course
    serializer_class = CourseSerializer

class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer

class BranchCreateView(generics.CreateAPIView):
    serializer_class = BranchSerializer

class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


