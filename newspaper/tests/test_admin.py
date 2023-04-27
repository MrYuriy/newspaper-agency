from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin1234",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="spiderman",
            password="spider1234",
            years_of_experience=10
        )

    def test_redactor_years_of_experience_listed(self):
        url = reverse("admin:newspaper_redactor_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.redactor.years_of_experience)
