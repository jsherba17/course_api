# import factory
# import factory.fuzzy
#
# from courses.models import Courses, Branches
#
#
# class CoursesFactory(factory.Factory):
# 	class Meta:
# 		model = Courses
# 	name = factory.Faker('name')
# 	description = factory.Faker('sentence')
# 	logo = factory.Faker('image_url')
#
# class BranchesFactory(factory.Factory):
# 	class Meta:
# 		model = Branches
# 	latitude = factory.Faker('name')
# 	longitude = factory.Faker('sentence')
# 	address = factory.Faker('')

from rest_framework.test import APIClient

client = APIClient()
client.post('/courses/', {'title': 'new idea'}, format='json')