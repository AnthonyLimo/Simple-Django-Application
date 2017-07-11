# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInLine(admin.StackedInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,        {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inline = [ChoiceInLine]

	list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)

