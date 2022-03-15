from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import TvShow


class TvShowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.tvshow = TvShow.objects.create(
            name="GOT", description="description test", rater=self.user, rating=5
        )

    def test_string_representation(self):
        self.assertEqual(str(self.tvshow), "GOT 5 tester")

    def test_tvshow_content(self):
        self.assertEqual(f"{self.tvshow.name}", "GOT")
        self.assertEqual(f"{self.tvshow.rater}", "tester")
        self.assertEqual(f"{self.tvshow.description}", "description test")
        self.assertEqual(f"{self.tvshow.rating}", "5")

    def test_tvshow_list_view(self):
        response = self.client.get(reverse("tvshow_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "GOT")
        self.assertTemplateUsed(response, "tvshow_list.html")

    def test_tvshow_detail_view(self):
        response = self.client.get(reverse("tvshow_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Rater: tester")
        self.assertTemplateUsed(response, "tvshow_detail.html")

    def test_tvshow_create_view(self):
        response = self.client.post(
            reverse("tvshow_create"),
            {
                "name": "Hawkeye",
                "description": "test",
                "rater": self.user.id,
            }, follow=True
        )

        self.assertTemplateUsed(response, "tvshow_create.html")
