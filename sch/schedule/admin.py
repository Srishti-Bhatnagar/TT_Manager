# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Schedule
from .models import Teacher
from .models import Batch
from .models import Subject

admin.site.register(Schedule)
admin.site.register(Batch)
admin.site.register(Subject)
admin.site.register(Teacher)
# Register your models here.
