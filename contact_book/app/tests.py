from django.test import TestCase
from django.urls import reverse

from .models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        from datetime import date
        self.contact = Contact.objects.create(
            name="John Doe",
            birthday=date(1990, 1, 1),
            email="john@email.com",
            phone="1234567890",
        )

    def test_contact_creation(self):
        self.assertEqual(self.contact.name, "John Doe")
        self.assertEqual(self.contact.birthday.strftime("%Y-%m-%d"), "1990-01-01")
        self.assertEqual(self.contact.email, "john@email.com")
        self.assertEqual(self.contact.phone, "1234567890")

    def test_contact_str(self):
        self.assertEqual(str(self.contact), "John Doe")


class ContactViewTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Jane Doe",
            birthday="1992-02-02",
            email="jane@email.com",
            phone="0987654321",
        )

    def test_contact_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")
        self.assertTemplateUsed(response, "contact_list.html")

    def test_contact_detail_view(self):
        response = self.client.get(f"/{self.contact.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jane Doe")
        self.assertTemplateUsed(response, "contact_detail.html")

    def test_contact_create_view(self):
        response = self.client.post(
            "/create/",
            {
                "name": "Alice Smith",
                "birthday": "1995-03-03",
                "email": "jane@email.com",
                "phone": "1122334455",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contact.objects.filter(name="Alice Smith").exists())

    def test_contact_update_view(self):
        response = self.client.post(
            f"/{self.contact.pk}/update/",
            {
                "name": "Jane Smith",
                "birthday": "1992-02-02",
                "email": "jane@email.com",
                "phone": "0987654321",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.name, "Jane Smith")

    def test_contact_delete_view(self):
        response = self.client.post(f"/{self.contact.pk}/delete/")
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Contact.objects.filter(id=self.contact.pk).exists())


class UrlTest(TestCase):
    def test_contact_list_url(self):
        url = reverse("contact_list")
        self.assertEqual(url, "/")

    def test_contact_detail_url(self):
        url = reverse("contact_detail", args=[1])
        self.assertEqual(url, "/1/")

    def test_contact_create_url(self):
        url = reverse("contact_create")
        self.assertEqual(url, "/create/")

    def test_contact_update_url(self):
        url = reverse("contact_update", args=[1])
        self.assertEqual(url, "/1/update/")

    def test_contact_delete_url(self):
        url = reverse("contact_delete", args=[1])
        self.assertEqual(url, "/1/delete/")
