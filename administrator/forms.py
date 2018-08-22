from django import forms
from cv.models import Experience, Education, Mycv

class ExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        # If the form.instance.pk it's None means that the form came from CreateView, so generate the Max value Order
        if self.instance.pk is None:
            self.initial['order'] = Experience.GetOrderMaxValue(Experience)
        
    position = forms.CharField(max_length=200, help_text='Enter a position', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your position'}),
                                                                                                    error_messages={'required': 'Please enter a Position.'})
    company = forms.CharField(max_length=200, help_text='Enter a Company', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Company'}))
    location = forms.CharField(max_length=200, help_text='Remember where you live!', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your current location'}))
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    order = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    #cv_experience = forms.ChoiceField(choices=[Mycv.objects.all().values()], widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Experience
        fields= ['position', 'company', 'location', 'startdate', 'description', 'image', 'order', 'cv_experience']
    
class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        # If the form.instance.pk it's None means that the form came from CreateView, so generate the Max value Order
        if self.instance.pk is None:
            self.initial['order'] = Education.GetOrderMaxValue(Education)
    
    university = forms.CharField(max_length=200, help_text='Enter a university', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your University'}))
    certification = forms.CharField(max_length=200, help_text='Enter a certification', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Certification'}))
    academic_discipline = forms.CharField(max_length=200, help_text='Enter a academic discipline', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Academic Discipline'}))
    mark = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
                                                       error_messages={'max_value': '10', 'min_value': '0'})
    startdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    activities = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    order = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Education
        fields= ['university', 'certification', 'academic_discipline', 'mark', 'startdate', 'description', 'activities', 'image', 'cv_education', 'order']
    
class ResumeForm(forms.ModelForm):
    display = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control form-check-input'}))

    class Meta:
        model = Mycv
        fields= ['display']