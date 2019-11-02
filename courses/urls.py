from django.urls import path
from courses import views

urlpatterns = [
    # path('courses/', views.course_list),
    # path('courses/<int:pk>/', views.course_detail),
    path('courses/createcat', views.CategoryCreateView.as_view()),
    path('courses/createbr', views.BranchCreateView.as_view()),
    path('courses/createcon', views.ContactCreateView.as_view()),
    path('courses/createcou', views.CourseCreateView.as_view()),
    path('courses/all', views.CourseListView.as_view()),
]