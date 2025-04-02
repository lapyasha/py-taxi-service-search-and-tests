from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Driver


class ModelTests(TestCase):
    def driver_str(self):
        driver = get_user_model().objects.create(
            username="test",
            password="test1234",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(driver),
            f"{driver.username} ({driver.first_name} {driver.last_name})"
        )

