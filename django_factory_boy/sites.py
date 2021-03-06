from django.contrib.sites.models import Site

import factory
import factory.django

__all__ = (
    'SiteFactory',
)


class SiteF(factory.django.DjangoModelFactory):
    FACTORY_FOR = Site

    name = factory.Sequence(lambda n: "site%s" % n)
    domain = factory.Sequence(lambda n: "site%s.com" % n)
