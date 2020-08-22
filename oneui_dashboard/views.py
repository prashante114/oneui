# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from django.template import RequestContext
# Create your views here.


def home(request):
	response = requests.get("http://hlx.li/tmp/lpb/payload.json?api_key=developer_key")
	if response.status_code ==200:
		response_json =json.loads(response.text)

		context={
			'response_list':response_json

		}

	return render(request, "oneui_dashboard.html",context)