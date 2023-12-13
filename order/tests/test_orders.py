from django.test import TestCase
from order.models import Order
from product.factories import ProductFactory
from django.contrib.auth.models import User


class OrderModelTest(TestCase):
    """Teste para o modelo de pedidos"""

    @classmethod
    def setUpTestData(cls):
        """Cria instâncias de teste para todos os métodos de teste.
        É executado apenas uma vez para cada classe de teste."""
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.product1 = ProductFactory.create()
        cls.product2 = ProductFactory.create()
        cls.order = Order.objects.create(user=cls.user)
        cls.order.product.add(cls.product1, cls.product2)

    def test_order_creation(self):
        """Teste para verificar a criação de um pedido"""
        self.assertTrue(isinstance(self.order, Order))
        self.assertEqual(self.order.user.username, "testuser")

    def test_order_with_products(self):
        """Teste para verificar um pedido com produtos"""
        self.assertEqual(self.order.product.count(), 2)
        self.assertIn(self.product1, self.order.product.all())
        self.assertIn(self.product2, self.order.product.all())
