from django.core.management import BaseCommand
from main.models import Student

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Hi, Sky!')
        student_list = [
            {'last_name': 'Муромец', 'first_name': 'Илья', 'is_active': False},
            {'last_name': 'Попович', 'first_name': 'Алеша', 'is_active': False},
            {'last_name': 'Никитич', 'first_name': 'Добрыня', 'is_active': False},
            {'last_name': 'Горыныч', 'first_name': 'Змей', 'is_active': False},
            {'last_name': 'Разбойник', 'first_name': 'Соловей', 'is_active': False},
            {'last_name': 'Волк', 'first_name': 'Серый', 'is_active': False},
            {'last_name': 'Горбунок', 'first_name': 'Конек', 'is_active': False},
            {'last_name': 'Прекрасная', 'first_name': 'Василиса', 'is_active': False},
            {'last_name': 'Лягушка', 'first_name': 'Царевна', 'is_active': False},
            {'last_name': 'Дурак', 'first_name': 'Иван', 'is_active': False},
            {'last_name': 'Яга', 'first_name': 'Баба', 'is_active': False}
        ]

        # for student_item in student_list:
        #     Student.objects.create(**student_item)


        students_for_create = []
        for student_item in student_list:
            students_for_create.append(Student(**student_item))

        Student.objects.bulk_create(students_for_create)
