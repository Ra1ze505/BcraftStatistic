from datetime import date

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.test import RequestFactory, Client

from .models import StaticItem


class StatisticTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        statistics = [StaticItem(date=date.today(), views=1, click=1, cost=1),
                      StaticItem(date=date(day=20, month=2, year=2000), views=2, cost=1.12),
                      StaticItem(date=date(day=10, month=3, year=2000), cost=21.36, click=213),
                      StaticItem(date=date(day=2, month=11, year=2000))]
        StaticItem.objects.bulk_create(statistics)

    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.client = Client()
        self.items = StaticItem.objects.all().order_by('-date')
        self.statistic_url = reverse('statistic:view-sets')

    def test_get_statistics(self):
        response = self.client.get(self.statistic_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for response_item, db_item in zip(response.data, self.items):
            self.assertEqual(response_item['id'], db_item.id)
            self.assertEqual(response_item['date'], str(db_item.date))
            if db_item.cost and db_item.click:
                self.assertEqual(response_item['cpc'], str(round(db_item.cost/db_item.click, 2)))
            if db_item.cost and db_item.views:
                self.assertEqual(response_item['cpm'], str(round(db_item.cost/db_item.views*1000, 2)))

    def test_create_statistic(self):
        data = {'date': '2022-12-31', 'views': 1000, 'click': 21343, 'cost': '13423.32'}
        response = self.client.post(self.statistic_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['date'], str(StaticItem.objects.get(id=response.data['id']).date))

    def test_remove_statistic(self):
        response = self.client.delete(self.statistic_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(StaticItem.objects.all().exists())


