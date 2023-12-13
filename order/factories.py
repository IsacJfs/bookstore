import factory

from django.contrib.auth.models import User
from product.factories import ProductFactory
from order.models import Order


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("pystr")
    email = factory.Faker("pystr")

    class Meta:
        model = User
        skip_postgeneration_save = True


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Order
        skip_postgeneration_save = True

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for produto in extracted:
                self.products.add(produto)
