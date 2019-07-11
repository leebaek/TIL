from django import forms
from .models import BS, BS2, Cost

year_choices = [tuple([x,x]) for x in range(2019,2031)]
month_choices = [tuple([x,x]) for x in range(1,13)]
day_choices = [tuple([x,x]) for x in range(1,32)]
hour_choices = [tuple([x,x]) for x in range(0,24)]
min_choices = [tuple([x,x]) for x in range(0,60,10)]
member_choices = [tuple([x,x]) for x in range(2,21)]
weight_choices = [tuple([x,x]) for x in range(1,11)]

class BSForm(forms.ModelForm):
    title = forms.CharField(
        label='모임명',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'title',
        })
    )
    year = forms.IntegerField(label="년도",
                              widget=forms.Select(choices=year_choices)
    )
    month = forms.IntegerField(label="월",
                              widget=forms.Select(choices=month_choices)
    )
    day = forms.IntegerField(label="일",
                              widget=forms.Select(choices=day_choices)
    )
    hour = forms.IntegerField(label="시",
                              widget=forms.Select(choices=hour_choices)
    )
    min = forms.IntegerField(label="분",
                              widget=forms.Select(choices=min_choices)
    )
    member = forms.IntegerField(label="인원수",
                                  widget=forms.Select(choices=member_choices)
    )

    class Meta:
        model = BS
        fields = ['title','year','month','day','hour','min','member']

class BS2Form(forms.ModelForm):#
    weight = forms.IntegerField(label="가중치",
                              widget=forms.Select(choices=weight_choices)
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
        model = BS2
        fields = ['weight','start','goal']

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