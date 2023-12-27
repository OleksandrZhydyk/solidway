from django.test import TestCase

from someapp.service import SomeModelService


class MockRepo:
    items = [f"item{i}" for i in range(20)]

    def get_items(self, page: int, per_page: int):
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        return self.items[start_index:end_index]


# Unit test to test business logic in the service layer
class TestSomeNodelService(TestCase):
    def setUp(self):
        self.service = SomeModelService(MockRepo())

    def test_get_items(self):
        items = self.service.get_items(2, 5)
        self.assertEqual(MockRepo.items[5:10], items)
