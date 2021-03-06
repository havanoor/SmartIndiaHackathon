from django import forms
from . models import Loan,LoanIssue

class LoanForm(forms.ModelForm):
	class Meta:
		model=Loan
		fields=('Amt','Rate','Year')

class ProcessLoan(forms.ModelForm):
	class Meta:
		model=LoanIssue
		fields=['Loan_Ref','Issued_To']