import json
import threading
from datetime import datetime

from django.http import HttpResponse

from hopw.settings import EMAIL_HOST_USER

from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context


# Global Variables
NOMBRE_INSTITUCION = 'HOP Contracting'

# TIPOS SERVICIOS
TIPO_SERVICIO_CONSTRUCTION = 1
TIPO_SERVICIO_REMODELING = 2
TIPO_SERVICIO_VOLTAGE = 3


def generate_file_name(nombre, original):
    ext = ""
    if original.find(".") > 0:
        ext = original[original.rfind("."):]
    fecha = datetime.now().date()
    hora = datetime.now().time()
    return nombre + fecha.year.__str__() + fecha.month.__str__() + fecha.day.__str__() + \
           hora.hour.__str__() + hora.minute.__str__() + hora.second.__str__() + ext


# Functions.py
class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, replyto=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.replyto = replyto
        threading.Thread.__init__(self)

    def run (self):
        try:
            headers = {}
            if self.replyto:
                headers['Reply-To'] = self.replyto
            msg = EmailMessage(self.subject, self.html_content, EMAIL_HOST_USER, self.recipient_list, headers=headers)
            msg.content_subtype = "html"
            msg.send()
        except:
            pass


def send_html_mail(subject, html_template, data, recipient_list, replyto=None):

    template = get_template(html_template)
    d = Context(data)
    html_content = template.render(d)

    EmailThread(subject, html_content, recipient_list, replyto).start()


def convertir_fecha(s):
    try:
        return datetime(int(s[-4:]), int(s[3:5]), int(s[:2]))
    except:
        return datetime.now()


def convertir_fecha_month_first(s):
    try:
        return datetime(int(s[-4:]), int(s[:2]), int(s[3:5]))
    except:
        return datetime.now()


def convertir_time(time):
    """
        t: array of integers 0-hour 1-minute
    """
    d = datetime.now().date()
    t = time.split(':')
    return datetime(d.year, d.month, d.day, int(t[0]), int(t[1]))


def bad_json(message=None, error=None, extradata=None):
    # Returns an invalid response on json data
    data = {'result': 'bad'}

    if message:
        data.update({'message': message})
    if error:
        if error == 0:
            data.update({"message": "Bad Request"})
        elif error == 1:
            data.update({"message": "Error saving data"})
        elif error == 2:
            data.update({"message": "Error updating data"})
        elif error == 3:
            data.update({"message": "Error deleting data"})
        elif error == 4:
            data.update({"message": "Permission Denied"})
        else:
            data.update({"message": "Server Error"})

    return HttpResponse(json.dumps(data), content_type="application/json")


def ok_json(data=None):
    # Returns a valid response on json data
    if data:
        if type(data) == dict and 'result' not in data.keys():
            data.update({"result": "ok"})
    else:
        data = {"result": "ok"}

    return HttpResponse(json.dumps(data), content_type="application/json")
