from django import forms
from .models import BS, Cost

class BSForm(forms.ModelForm):
    year = forms.IntegerField(
        label='년도',
        widget=forms.DateInput(attrs={
            'class':'year',
        })
    )
    month = forms.IntegerField(
        label='월',
        widget=forms.DateInput(attrs={
            'class':'month',
        })
    )
    day = forms.IntegerField(
        label='일',
        widget=forms.DateInput(attrs={
            'class':'day',
        })
    )
    hour = forms.IntegerField(
        label='시',
        widget=forms.DateInput(attrs={
            'class':'hour',
        })
    )
    min = forms.IntegerField(
        label='분',
        widget=forms.DateInput(attrs={
            'class':'min',
        })
    )
    title = forms.CharField(
        label='모임명',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
        })
    )
    member = forms.IntegerField(
        label='인원수',
        widget=forms.NumberInput(attrs={
            'class':'member',
        })
    )
    weight = forms.IntegerField(
        label='가중치',
        widget=forms.NumberInput(attrs={
            'class':'weight',
        })
    )
    start = forms.CharField(
        label='출발지',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class':'start',
        })
    )
    goal = forms.CharField(
        label='목적지',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class':'goal',
        })
    )
    class Meta:
        model = BS
        fields = ['year','month','day','hour','min','title','member','weight','start','goal']

class CostForm(forms.ModelForm):
    cost = forms.IntegerField(
        label='총 결제비용',
        widget=forms.NumberInput(attrs={
            'class':'cost',
        })
    )
    class Meta:
        model = Cost
        fields = ['cost']