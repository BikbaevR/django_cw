from django.contrib import admin

from .models import Request
from .models import *

admin.site.register([Request, Resume, Vacancy, Skills, Company])
