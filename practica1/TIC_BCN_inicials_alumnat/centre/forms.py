from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        field = ['id', 'first_Name', 'last_Name', 'age']
        fields = '__all__'