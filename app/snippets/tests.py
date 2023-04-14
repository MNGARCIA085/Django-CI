from django.test import TestCase

# Create your tests here.


"""
title y code
"""

from rest_framework.test import APIRequestFactory,APIClient
from rest_framework import status

# Using the standard RequestFactory API to create a form POST request
#factory = APIRequestFactory()
#request = factory.post('/notes/', {'title': 'new idea'})




from .models import Snippet


import json




class SnippetTestCase(TestCase):
    
    
    
    def setUp(self):
        snippet = Snippet(
            title='vamos',
            code='for in in range(0,100)',
        )
        snippet.save()
    

    def test_get_snippet(self):
        """Get sniṕpets"""
        client = APIClient()
        response = client.get('/snippets/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        print(content)
        self.assertEqual(len(content),1)
        self.assertEqual('id' in content[0], True)






class UserTestCase(TestCase):
    
    
    """
    def setUp(self):
        snippet = Snippet(
            title='vamos',
            code='for in in range(0,100)',
        )
        snippet.save()
    """

    def test_signup_user(self):
        """Check if we can create a snippet"""


        print('snps',Snippet.objects.all().count())

        client = APIClient()
        response = client.post(
                '/snippets/', {
                'title': 'dsfdsfdsfdsfdsfdsfsd',
                'code': 'nico'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #self.assertEqual(json.loads(response.content), {"username":"testing1","first_name":"Testing","la







#https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Testing




"""
class YourTestClass(TestCase):

    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(self):
        #Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)


"""