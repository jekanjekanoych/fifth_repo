import random

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from faker import Faker

from .models import Teacher


def index(request):
    return HttpResponse({"Main Page"})


def teacher(request):
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    age = random.randrange(25, 60)
    teacher = Teacher.objects.create(
        first_name=first_name, last_name=last_name, age=age
    )
    get_teacher = Teacher.objects.all()
    return render(request, "generate-teacher.html", {"get_teacher": get_teacher})
