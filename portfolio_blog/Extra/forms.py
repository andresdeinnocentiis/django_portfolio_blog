from django import forms




class AddStudyForm(forms.Form):

    name = forms.CharField(max_length=100)
    type = forms.CharField(max_length=100)
    institution = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea,required=False)
    from_date = forms.DateField()
    to_date = forms.DateField()
    institution_link = forms.CharField(max_length=100,required=False)
    certificate_link = forms.CharField(max_length=100,required=False)


class AddTechnologyForm(forms.Form):

    name = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    years_exp = forms.FloatField(min_value=0.0)