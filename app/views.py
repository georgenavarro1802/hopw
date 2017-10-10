import datetime
from django.shortcuts import render

from app.functions import ok_json, send_html_mail, bad_json
from app.models import Aboutus, Services, Whyus, Projects, Team, Newsletter, Clients, CONTACT_TYPES, Company, Contacts, \
    Construction
from hopw.settings import EMAIL_ACTIVE, SUSCRIPCION_EMAILS


def index(request):

    # About Us
    last_aboutus = Aboutus.objects.all()[0] if Aboutus.objects.exists() else None
    words_aboutus = last_aboutus.words.split(',') if last_aboutus else []

    # Services
    last_service = Services.objects.all()[0] if Services.objects.exists() else None

    # Why Choose Us
    last_whyus = Whyus.objects.all()[0] if Whyus.objects.exists() else None

    # Projects
    last_project = Projects.objects.all()[0] if Projects.objects.exists() else None

    # Teams
    last_team = Team.objects.all()[0] if Team.objects.exists() else None

    # Clients
    last_client = Clients.objects.all()[0] if Clients.objects.exists() else None

    # Contacts
    contact_types = CONTACT_TYPES

    # Company
    company = Company.objects.all()[0]

    return render(request,
                  "index.html",
                  {
                      'aboutus': last_aboutus,
                      'aboutus_words': words_aboutus,
                      'service': last_service,
                      'whyus': last_whyus,
                      'project': last_project,
                      'team': last_team,
                      'client': last_client,
                      'contact_types': contact_types,
                      'company': company,
                  })


def newsletter(request):

    if request.method == 'POST':

        if 'email' in request.POST and request.POST['email']:
            email = request.POST['email']

            if Newsletter.objects.filter(email=email).exists():
                return ok_json(data={'message': 'Email already exist in our database'})

            # Create newsletter and save it
            newsletter = Newsletter(email=email, created=datetime.datetime.now())
            newsletter.save()

            if EMAIL_ACTIVE:
                send_html_mail("HOP Website - Newsletter", "newsletter.html",
                               {'newsletter': newsletter, 'total': Newsletter.objects.count()},
                               SUSCRIPCION_EMAILS)

            return ok_json(data={'message': 'Suscription created successfully. Thanks to be part of HOP Contracting'})

    return bad_json(error=0)


def contact(request):

    if request.method == 'POST':

        first_name = ''
        if 'contact-first-name' in request.POST and request.POST['contact-first-name']:
            first_name = request.POST['contact-first-name']

        last_name = ''
        if 'contact-last-name' in request.POST and request.POST['contact-last-name']:
            last_name = request.POST['contact-last-name']

        email = ''
        if 'contact-email' in request.POST and request.POST['contact-email']:
            email = request.POST['contact-email']

        type = None
        if 'contact-type' in request.POST and request.POST['contact-type']:
            type = int(request.POST['contact-type'])

        message = ''
        if 'contact-message' in request.POST and request.POST['contact-message']:
            message = request.POST['contact-message']

        if first_name and last_name and email and message:

            # Create contact and data related with
            contact = Contacts(first_name=first_name,
                               last_name=last_name,
                               email=email,
                               contact_type=type,
                               message=message,
                               created=datetime.datetime.now())
            contact.save()

            if EMAIL_ACTIVE:
                send_html_mail("HOP Website - New Contact", "contact.html",
                               {'contact': contact, 'total': Contacts.objects.count()},
                               SUSCRIPCION_EMAILS)

                return ok_json(data={'message': 'Your message has been received successfully. '
                                                'Your opinion is important for us. We will be in touch soon. Thanks'})

        return bad_json(message='Please fill all the fields before to send the form, thanks.')

    return bad_json(error=0)


def construction(request):

    # Company
    company = Company.objects.all()[0] if Company.objects.exists() else None

    # Construction
    construction = Construction.objects.all()[0] if Construction.objects.exists() else None

    return render(request, 'construction.html',
                  {
                      'company': company,
                      'construction': construction
                  })
