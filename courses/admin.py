from django.contrib import admin
from courses.models import Course, Category, Branch, Contact

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Contact)