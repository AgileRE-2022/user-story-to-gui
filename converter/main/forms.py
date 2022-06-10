from django import forms
from .models import UserStory

class UserStoryForm(forms.Modelform):
	class Meta:
		model = UserStory
		fields = ['role','task','benefit','initState','action','result']