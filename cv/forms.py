from django import forms
from cv.models import Experience, Education, Mycv

class ExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        pass
        
    position = forms.CharField(max_length=200, help_text='Enter a position', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your position'}),
                                                                                                    error_messages={'required': 'Please enter a Position.'})
    company = forms.CharField(max_length=200, help_text='Enter a Company', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Company'}))
    location = forms.CharField(max_length=200, help_text='Remember where you live!', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your current location'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    #cv_experience = forms.ChoiceField(choices=[Mycv.objects.all().values()], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Experience
        fields= ['position', 'company', 'location', 'startdate', 'description', 'cv_experience']
        