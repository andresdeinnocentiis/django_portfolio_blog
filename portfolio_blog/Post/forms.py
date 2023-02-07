from django import forms


class AddReviewForm(forms.Form):
    
    rating = forms.FloatField(min_value = 0.0, max_value = 5.0, required=True)
    content = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        
        super().__init__(*args, **kwargs)
        if not self.user.is_authenticated:
            self.fields['user'] = forms.CharField(required=True)

    class Meta:
        field_order = ['user', 'rating', 'content']



class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    caption = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea)
    tech_used = forms.CharField(widget=forms.Textarea)
    github_link = forms.CharField(max_length=100, required=False)
    website_link = forms.CharField(max_length=100, required=False)
    








