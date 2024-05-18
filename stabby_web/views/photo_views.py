import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from stabby_web.dtos import TemplateVariableDTO
from stabby_web.forms import WorkLogForm
from stabby_web.models import Knife
from stabby_web.services import WorkLogService, KnifeService, SharpenerService
from stabby_web.enums import FormTypes, Modules, ViewTypes
from django.contrib.auth.decorators import login_required