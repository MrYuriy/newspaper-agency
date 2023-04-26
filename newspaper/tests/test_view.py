from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Redactor, Newspaper

topic_create_url = reverse("newspaper:topic-create")
newspaper_list_url = reverse("newspaper:newspaper-list")
redactor_list_url = reverse("newspaper:redactor-list")


class PublicTopicCreateTest(TestCase):
    def test_login_required(self):
        response = self.client.get(topic_create_url)
        self.assertNotEqual(response.status_code, 200)


class PrivateRedactorTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user",
            password="password",
        )
        self.client.force_login(self.user)

    def test_create_redactor(self):
        form_data = {
            "username": "Username",
            "password1": "password12!",
            "password2": "password12!",
            "first_name": "first_name",
            "last_name": "last_name",
            "years_of_experience": 2
        }
        self.client.post(
            reverse("newspaper:redactor-create"),
            data=form_data
        )
        created_user = get_user_model().objects.get(
            username=form_data["username"]
        )

        self.assertEqual(created_user.first_name, form_data["first_name"])
        self.assertEqual(created_user.last_name, form_data["last_name"])
        self.assertEqual(
            created_user.years_of_experience,
            form_data["years_of_experience"]
        )


class PublicRedactorListTests(TestCase):
    def setUp(self) -> None:
        Redactor.objects.create(
            username="Test1",
            first_name="Test1",
            last_name="Driver",
            years_of_experience=22
        )

        Redactor.objects.create(
            username="Test2",
            first_name="Test2",
            last_name="Driver",
            years_of_experience=2
        )

        Redactor.objects.create(
            username="Test3",
            first_name="Test3",
            last_name="Driver",
            years_of_experience=8
        )

        Redactor.objects.create(
            username="Test4",
            first_name="Test4",
            last_name="Driver",
            years_of_experience=5
        )
        Redactor.objects.create(
            username="Test5",
            first_name="Test5",
            last_name="Driver",
            years_of_experience=5
        )

    def test_redactor_list_pagination_is_tree(self):
        response = self.client.get(redactor_list_url)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["redactor_list"]), 3)

    def test_lists_all_redactors(self):
        response = self.client.get(redactor_list_url + "?page=2")
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["redactor_list"]), 2)


class PublicNewspaperListTest(TestCase):
    def setUp(self) -> None:
        Newspaper.objects.create(
            title="Test",
            content="Test content"
        )
        Newspaper.objects.create(
            title="Test2",
            content="Test content2"
        )
        Newspaper.objects.create(
            title="Test3",
            content="Test content3"
        )
        Newspaper.objects.create(
            title="Test4",
            content="Test content4"
        )

    def test_retrieve_newspaper_list(self):

        response = self.client.get(newspaper_list_url)
        newspapers = Newspaper.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "newspaper/newspaper_list.html"
        )

    def test_newspaper_list_pagination_is_tree(self):
        Newspaper.objects.create(
            title="Test5",
            content="Test content5"
        )
        response = self.client.get(newspaper_list_url)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["newspaper_list"]), 3)

    def test_lists_all_newspapers(self):
        Newspaper.objects.create(
            title="Test5",
            content="Test content5"
        )
        response = self.client.get(newspaper_list_url + "?page=2")
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)

    def test_newspaper_filter_by_title_is_valid(self):
        newspaper1 = Newspaper.objects.create(
            title="New Test5",
            content="Test content5"
        )

        response = self.client.get(newspaper_list_url + "?title=new")
        self.assertEqual(
            list(response.context["newspaper_list"]),
            [newspaper1]
        )