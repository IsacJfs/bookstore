from django.test import TestCase
from product.models import Product, Category
from product.factories import ProductFactory, CategoryFactory

class ProductModelTest(TestCase):
    """Teste para o modelo de produtos"""
    @classmethod
    def setUpTestData(cls):
        """Cria instâncias de teste para todos os métodos de teste.
        É executado apenas uma vez para cada classe de teste."""
        cls.category = CategoryFactory.create()
        cls.product = ProductFactory.create(title="Test Product", price=100, active=True)
        cls.product.category.add(cls.category)

    def test_product_creation(self):
        """Teste para verificar a criação de um produto"""
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.title, "Test Product")
        self.assertEqual(self.product.price, 100)
        self.assertTrue(self.product.active)
        self.assertIn(self.category, self.product.category.all())

    def test_product_representation(self):
        """Teste para verificar a representação de um produto"""
        self.assertEqual(str(self.product), "Test Product")

