from django.core.management.base import BaseCommand, CommandError
from polls.models import Teacher
from faker import Faker
from django.http import HttpResponse, JsonResponse

import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("teachers", type=int)

    def handle(
        self,
        *args,
        teachers,
        **options,
    ):
        # teachers = options["teachers"]

        for _ in range(teachers):
            fake = Faker()
            # f = []
            # first_name = fake.first_name()
            # f.append(first_name)
            # l =[]
            # last_name = fake.last_name()
            # l.append(last_name)
            # a = []
            # age = random.randrange(25, 60)
            # a.append(age)
            list_teachers = [
                Teacher(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    age=random.randrange(25, 60),
                )
            ]
            teacher = Teacher.objects.bulk_create(list_teachers)
            self.stdout.write(
                self.style.SUCCESS('Successfully created Teacher "%s"' % teacher)
            )
            get_teachers = Teacher.objects.all()

        return HttpResponse({get_teachers})

        # for _ in range(teachers):
        #     t = Teacher.objects.create(first_name=first_name, last_name=last_name, age=age)
        #     self.stdout.write(self.style.SUCCESS('Successfully created Teacher with ID "%s"' % t.id))
