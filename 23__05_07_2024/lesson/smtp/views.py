from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string


def index(request):
    body = '<h1>Hello</h1>'

    file_content = open('smtp/urls.py', 'rb').read()

    body_from_template = render_to_string(template_name='smtp/index.html', request=request, context={
        'name': 'Rafael'
    })

    message = EmailMessage(
        subject='Django-test',
        body=body_from_template,
        to=['rafael.bikbayev@gmail.com'],
        attachments=[('test.py', file_content), ('test1.py', file_content)]
    )

    message.content_subtype = 'html'
    # message.attach('test_file.py', file_content)

    message.send()

    return HttpResponse("Hello, world. You're at the polls index.")
