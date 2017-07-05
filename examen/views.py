# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Contact


# Create your views here.
class IndexView (ListView):

	template_name = 'index.html'
	model = Contact

class ContactoDetailView (ListView):

	template_name = 'contacto.html'
	model = Contact