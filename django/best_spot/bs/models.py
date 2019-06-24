from django.db import models

class BS(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    min = models.IntegerField()
    title = models.CharField(max_length=20)
    member = models.IntegerField()
    weight = models.IntegerField()
    start = models.CharField(max_length=10)
    goal = models.CharField(max_length=10)

    def __str__(self):
        return f'날짜: {self.year}년 {self.month}월 {self.day}일 {self.hour}시 {self.min}분'

# 약속 만들기
class Meeting(models.Model):
    date = models.DateField() # Calendar_1.html의 날짜
    time = models.DateTimeField()  # Calendar_2.html의 Time
    title = models.CharField(max_length=20) # Calendar_2.html의 모임 주제
    memo = models.CharField(max_length=20) # Calendar_2.html의 메모
    member = models.IntegerField()  # Calendar_2.html의 인원 수

    def __str__(self):
        return f'날짜: {self.date} 시간:{self.time} 주제:{self.title} 메모:{self.memo}'

# 장소 정하기 / Meeting과 1:N 관계
class Map(models.Model):
    weight = models.IntegerField() # 가중치
    start = models.CharField(max_length=20)
    goal = models.CharField(max_length=20)
    lat = models.FloatField() # 좌표의 위도값
    lng = models.FloatField() # 좌표의 경도값
    matching_1_lat = models.FloatField() # 1차 매칭된 좌표의 위도값
    matching_1_lng = models.FloatField() # 1차 매칭된 좌표의 경도값
    matching_1_name = models.CharField(max_length=20) # 2차 매칭 위치 이름
    matching_2_lat = models.FloatField() # 2차 매칭된 좌표의 위도값
    matching_2_lng = models.FloatField() # 2차 매칭된 좌표의 경도값
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)

# 결산 / Meeting과 1:N 관계
class Cost(models.Model):
    money = models.IntegerField()
    cost = models.ForeignKey(Meeting, on_delete=models.CASCADE)

    def __str__(self):
        return f'총 결제금액: {self.cost}원'