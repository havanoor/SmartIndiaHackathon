from django import forms
from . models import Loan

class LoanForm(forms.ModelForm):
	class Meta:
		model=Loan
		fields=('Amt','Rate','Year')