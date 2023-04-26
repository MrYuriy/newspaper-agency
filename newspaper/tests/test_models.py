from django.contrib.auth import get_user_model
from django.test import TestCase

from newspaper.models import Topic, Newspaper


class ModelTests(TestCase):
    def test_redactor_str(self):
        redactor = get_user_model().objects.create_user(
            username="username",
            password="password",
            first_name="firstname",
            last_name="lastname",
            years_of_experience=2,
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )
        self.assertEqual(redactor.years_of_experience, 2)
        self.assertTrue(redactor.check_password("password"))
        self.assertEqual(redactor.username, "username")
        self.assertEqual(redactor.first_name, "firstname")
        self.assertEqual(redactor.last_name, "lastname")

    def test_topic_str(self):
        topic = Topic.objects.create(
            name="Topic",
        )
        self.assertEqual(str(topic), topic.name)

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.create(
            title="Title",
            content="Newspaper content",
        )
        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} - {newspaper.published_date}"
        )
