from django.test import TestCase
from product.serializers import CategorySerializer
from product.models import Category

class CategorySerializerTestCase(TestCase):
    """Teste para o serializer de categorias"""
    def setUp(self):
        """Configuração dos testes, executado uma vez antes de cada teste"""
        self.category_attributes = {
            'title': 'Categoria Teste',
            'slug': 'categoria-teste',
            'description': 'Descrição da categoria',
            'active': True
        }
        self.serializer_data = self.category_attributes
        self.category = Category.objects.create(**self.category_attributes)
        self.serializer = CategorySerializer(instance=self.category)

    def test_contains_expected_fields(self):
        """Teste para verificar os campos do serializer"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['title', 'slug', 'description', 'active']))

    def test_title_field_content(self):
        """Teste para verificar o conteúdo do campo title"""
        data = self.serializer.data
        self.assertEqual(data['title'], self.category_attributes['title'])

class CategoryModelTest(TestCase):
    """Teste para o modelo de categorias"""
    def setUp(self):
        """Configuração dos testes"""
        self.category = Category.objects.create(
            title='Categoria Teste',
            slug='categoria-teste',
            description='Descrição da categoria',
            active=True
        )

    def test_category_creation(self):
        """Teste para verificar a criação de uma categoria"""
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.title)

