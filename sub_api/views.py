from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import *

from .serializers import SubscriptionsSerializer
from .models import Subscriptions
from .forms import SubForm
from .validations import email_validate
from .err import *

class SubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = Subscriptions.objects.all().order_by('email')
    serializer_class = SubscriptionsSerializer

# Create your views here.
def index(request):
    return render(request,'index.html',context={'success': 'False','error_msg':''})

def add_email_form(request):

    if request.method == 'POST':
        post_data = request.POST.copy()


        em = post_data.get("email", None)
        if not email_validate(em):
            return render(request,'index.html',context={'success': 'False','error_msg':EMAIL_INVALID})
        try:
            sub_inst = Subscriptions.objects.get(email=em)
            return render(request,'index.html',context={'success': 'False','error_msg':EMAIL_EXISTS})
        except ObjectDoesNotExist as e:
            sub_inst = Subscriptions()
            sub_inst.email = em
            sub_inst.save()
            print("instance saved")
            return render(request,'index.html',context={'success': 'True','error_msg':EMAIL_SUC})

    else:
        return render(request,'index.html',context={})

    return render(request,'index.html',context={})