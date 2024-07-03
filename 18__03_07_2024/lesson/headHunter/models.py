from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=100)
    # exp = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy')
    salary = models.IntegerField()
    skills = models.ManyToManyField(Skills, related_name='vacancy_skills')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    job_types = [('FULL_TIME', 'Полная занятость'),
                 ('PART_TIME', 'Частичная занятость'),
                 ('REMOTE', 'Удаленная работа')]
    type_of_job = models.CharField(max_length=100, choices=job_types)

    def __str__(self):
        return self.title

class Resume(models.Model):
    dream_job = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    skills = models.ManyToManyField(Skills, related_name='resume_skills')
    exp = models.CharField(max_length=100)
    education_type = [('SCHOOL', 'Школьное'),
                      ('BAKALAVR', 'Бакалавр'),
                      ('PROFESSOR', 'Профессор'),
                      ('MAGISTER', 'Магистр')]
    education = models.CharField(max_length=100, choices=education_type)
    gender_type = [('MALE', 'Муж.'),
                   ('FEMALE', 'Жен.'),
                   ('OTHER', 'Другое')]
    gender = models.CharField(max_length=100, choices=gender_type)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')

    def __str__(self):
        return self.dream_job

class Request(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='request')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='request')
    created_at = models.DateTimeField(auto_now_add=True)
    status_type = [('NEW', 'Новый'),
                   ('ACCEPT', 'Принят'),
                   ('RECALL', 'Перезвонят')]
    status = models.CharField(max_length=100, choices=status_type)

    def __str__(self):
        return self.status