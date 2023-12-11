import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(title="mouse", price=100)
        self.product.category.add(self.category)
        self.user = UserFactory()
        self.order = OrderFactory(user=self.user)
        self.order.product.add(self.product)

    def test_order(self):
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)
        print(order_data)
        first_order = order_data["results"][0]
        self.assertEqual(
            first_order["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            first_order["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            first_order["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            first_order["product"][0]["category"][0]["title"],
            self.category.title,
        )

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"user": user.id, "products_id": [product.id]})
        print(data)
        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)
        created_order.product.add(product.id)
