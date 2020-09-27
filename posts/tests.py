from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='ya', password='password')
        test_user.save()

        test_post = Post.objects.create(
            author = test_user,
            title = 'banana',
            body = 'apple'
        )
        test_post.save() # Save the object to mock Database

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'ya')
        self.assertEqual(actual_title, 'banana')
        self.assertEqual(actual_body, 'apple')

