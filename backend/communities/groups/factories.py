# SPDX-License-Identifier: AGPL-3.0-or-later
import datetime
import random

import factory

from communities.groups.models import (
    Group,
    GroupImage,
    GroupMember,
    GroupSocialLink,
    GroupText,
)

# MARK: Group


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    created_by = factory.SubFactory("authentication.factories.UserFactory")
    name = factory.Faker("word")
    tagline = factory.Faker("word")
    creation_date = factory.LazyFunction(
        lambda: datetime.datetime.now(tz=datetime.timezone.utc)
    )
    terms_checked = factory.Faker("boolean")
    category = factory.Faker("word")
    location = factory.SubFactory("content.factories.EntityLocationFactory")


# MARK: Bridge Tables


class GroupImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupImage

    group = factory.SubFactory(GroupFactory)
    image = factory.SubFactory("content.factories.ImageFactory")


class GroupMemberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupMember

    group = factory.SubFactory(GroupFactory)
    user = factory.SubFactory("authentication.factories.UserFactory")
    is_admin = factory.Faker("boolean")


class GroupSocialLinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupSocialLink

    link = "https://www.activist.org"
    label = "social link"
    order = random.randint(0, 10)
    creation_date = factory.LazyFunction(
        lambda: datetime.datetime.now(tz=datetime.timezone.utc)
    )
    last_updated = factory.LazyFunction(
        lambda: datetime.datetime.now(tz=datetime.timezone.utc)
    )


class GroupTextFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupText

    iso = "en"
    primary = factory.Faker("boolean")
    description = factory.Faker(provider="text", locale="la", max_nb_chars=1000)
    get_involved = factory.Faker(provider="text", locale="la")
    donate_prompt = factory.Faker(provider="text", locale="la")
