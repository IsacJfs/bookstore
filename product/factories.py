import factory

from product.models import Product
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    id = factory.Faker("pyint")
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    price = factory.Faker("pyint")
    category = factory.LazyAttribute(CategoryFactory)

    class Meta:
        model = Product
        skip_postgeneration_save = True

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for categories in extracted:
                self.category.add(categories)
