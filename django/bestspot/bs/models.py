from django.db import models
from django.conf import settings

class BS(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    min = models.IntegerField()
    title = models.CharField(max_length=20)
    member = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'날짜: {self.year}년 {self.month}월 {self.day}일 {self.hour}시 {self.min}분 {self.member}명'

class BS2(models.Model):
    weight = models.IntegerField(blank=True)
    start = models.CharField(max_length=20)
    goal_lat = models.FloatField()
    goal_lng = models.FloatField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Cost(models.Model):
    cost = models.IntegerField()

    def __str__(self):
        return f'총 결제금액: {self.cost}원'
