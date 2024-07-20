import os, django, random, sys
from pathlib import Path
from faker import Faker
from validate_docbr import CPF

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.join(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from apps.school.models import Student

def run():
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(50):
        cpf = CPF()
        name = fake.name()
        email = '{}@{}'.format(name.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        birth_date = fake.date_of_birth(minimum_age=18, maximum_age=30)
        phone = "{} 9{}-{}".format(random.randrange(10, 89), random.randrange(4000, 9999), random.randrange(4000, 9999))
        Student.objects.create(
            name=name,
            email=email,
            cpf=cpf,
            birth_date=birth_date,
            phone=phone
        )
run()