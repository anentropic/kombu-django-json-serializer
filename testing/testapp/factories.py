from datetime import datetime

import factory
import factory.fuzzy

from .models import Customer, Example


class CustomerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.fuzzy.FuzzyText()


class ExampleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Example

    customer = factory.SubFactory(CustomerFactory)
    name = factory.fuzzy.FuzzyText()
    count = factory.fuzzy.FuzzyInteger(0, 42)
    created = factory.fuzzy.FuzzyNaiveDateTime(datetime(2008, 1, 1),
                                               datetime(2009, 1, 1))
    birthday = factory.fuzzy.FuzzyDate(datetime(2008, 1, 1),
                                       datetime(2009, 1, 1))
    price = factory.fuzzy.FuzzyDecimal(0.5, 42.7)
