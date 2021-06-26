import factory

from orpha_lookup.apps.orpha.models import Disorder, DisorderType, DisorderGroup, Frequency, Hpo, DisorderHpos


class DisorderTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DisorderType

    name = factory.Faker('sentence', nb_words=2)


class DisorderGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DisorderGroup

    name = factory.Faker('sentence', nb_words=2)


class FrequencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Frequency

    name = factory.Faker('sentence', nb_words=2)
    weight = factory.Faker('random_int', max=100)


class HpoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Hpo

    hpo_id = factory.Faker('numerify', text='HP:######')
    name = factory.Faker('sentence', nb_words=2)


class DisorderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Disorder

    orpha_code = factory.Faker('random_int', max=1000000)
    expert_link = factory.Faker('uri')
    name = factory.Faker('sentence', nb_words=2)
    disorder_type = factory.SubFactory(DisorderTypeFactory)
    disorder_group = factory.SubFactory(DisorderGroupFactory)


class DisorderHposFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DisorderHpos

    disorder = factory.SubFactory(DisorderFactory)
    hpo = factory.SubFactory(HpoFactory)
    frequency = factory.SubFactory(FrequencyFactory)
