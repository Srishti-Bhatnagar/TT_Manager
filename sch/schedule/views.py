# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from schedule.models import Batch,Teacher,Schedule,Subject
# Create your views here.
def batch_home(request):
	
	
	b=Batch.objects.get(stream="CSE")
	tt=b.TT.all()
	return render(request, 'schedule/batch_home.html',{'tt':tt})
