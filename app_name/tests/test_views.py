from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from djang.utils.html import escape
from app_name.models import * # Change this when we have models to import
# Probably import app_name.forms and views as well


class SomeViewTest(TestCase):

	def test_something_about_a_view(self):
		pass

