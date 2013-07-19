from django.test import TestCase


class RecollectTest(TestCase):

    def test_home(self):

        response = self.client.get('/')
        print dir(response)
        self.assertContains(response, 'world', 1, 200)
