from django import forms
from crud.models import ClassRoom

class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)


class ClassRoomModelForm(forms.ModelForm):
    # is_active = forms.BooleanField() for extra field
    class Meta:
        model = ClassRoom
        fields = ["name",]