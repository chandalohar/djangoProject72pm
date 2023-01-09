from django import forms
from.models import Reg
class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        fields=['firstname','lastname','username','password','cpassword','mailid','mobno']
        widgets={'password':forms.PasswordInput(),
                 'cpassword':forms.PasswordInput()}
