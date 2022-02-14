from django.core.checks import messages
from django.http import request
from rest_framework.response import Response

from ..models import Measurement
from ..models import Variable


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement


def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.value = new_var["value"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(variable=Variable.objects.get(name=var["variable"]), value=var["value"], unit=var["unit"],
                              place=var["place"])
    measurement.save()
    return measurement


def delete_measurement(var_pk):
    measurement = get_measurement(var_pk)
    measurement.delete()
    return measurement
