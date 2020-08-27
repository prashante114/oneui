# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
	
	return render(request, "oneui_dashboard.html",{})