from django import forms

from .models import Post, Language_log

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('postname', 'contents',)



class SpeakingForm(forms.ModelForm):

    class Meta:
        model = Language_log
        fields = ('who', 'where','startDate','endDate','topic','summary')        

class ReadingForm(forms.ModelForm):

    class Meta:
        model = Language_log
        fields = ('what', 'startDate','endDate','summary')                