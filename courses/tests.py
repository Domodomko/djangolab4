from django.test import TestCase
from courses.models import Course, Contact, Category, Branch


class CourseModelTest(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='language', imgpath='sadad.png')

    def test_course(self):
        course1 = Course.objects.create(name='Funny English', description='kek', category=self.category1, logo='dsadad.png', )
        branch1 = Branch.objects.create(latitude='231321', longitude='123131', address='dasdadadsda', course=course1)
        contact1 = Contact.objects.create(type='FACEBOOK', value='sdadakdada', course=course1, )
        contact2 = Contact.objects.create(type='EMAIL', value='sadadasdada', course=course1, )

        self.assertEqual(self.category1.name, 'language')
        self.assertEqual(course1.name, 'Funny English')
        self.assertEqual(branch1.latitude, '231321')
        self.assertEqual(contact1.type, 'FACEBOOK')
        self.assertEqual(contact2.value, 'sadadasdada')