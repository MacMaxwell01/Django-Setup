from django.test import TestCase
from django.urls import reverse


class PostCardPageTests(TestCase):
    def test_post_page_renders_post_card_layout(self):
        response = self.client.get(reverse("post"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "post-card")
        self.assertContains(response, "Post Card")


class HomePageTests(TestCase):
    def test_home_page_renders_a_polished_landing_view(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Explore the site")
        self.assertContains(response, "About")
