from django.forms import ModelForm 
from mysqlapp.models import Userimages


class UserForm(ModelForm):
	class Meta:
		model=Userimages
		fields='__all__'