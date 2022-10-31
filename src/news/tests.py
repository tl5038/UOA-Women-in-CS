from django.db import IntegrityError
from django.test import Client, TestCase
from django.urls import reverse

from news.models import NewsModel


class NewsTestCase(TestCase):
    def setUp(cls):
        NewsModel.objects.create(
            title="test 1",
            body="test 1 description",
            subtitle="test 1 subtitle",
        )

    def test_news_model(self):
        test1 = NewsModel.objects.get(title="test 1")
        self.assertEqual(test1.body, "test 1 description")

        with self.assertRaises(IntegrityError):
            NewsModel.objects.create(title="test 2", body="test 2 description")

    def test_news_page(self):
        client = Client()
        response = client.get("/news/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("test 1", str(response.content))

    def test_unique_slug(self):
        NewsModel.objects.create(title="test 1", body="test 1 description", subtitle="test 1 subtitle")
        self.assertEqual(NewsModel.objects.count(), 2)
        self.assertEqual(NewsModel.objects.get(slug="test-1").title, "test 1")
        self.assertEqual(NewsModel.objects.get(slug="test-1-2").title, "test 1")

    def test_news_not_exist(self):
        response = self.client.get(reverse("news-single", kwargs={"slug": "does-not-exist"}))
        self.assertEqual(response.status_code, 404)
