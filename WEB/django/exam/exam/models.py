from django.db import models

# 필드 기본 옵션
# null, blank = 디폴트 False

# Person 테이블
# first_name : 단문
# last_name : 단문
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # 데이터베이스에서 기본적으로 '앱이름_테이블명' 이렇게 만들어진다.
    class Meta:
        db_table = "person"  # 이렇게 해주면 테이블명을 직접 지어주는 것.

    # __str__ 함수는 makemigrations(migrate) 대상이 아님
    def __str__(self):
        return self.first_name + ", " + self.last_name


# Musician 테이블
# first_name : 단문
# last_name : 단문
# instrument : 단문
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    class Meta:
        db_table = "musician"

    def __str__(self) -> str:
        return self.first_name + ", " + self.instrument


# Album 테이블
# artist : 외래키(FK) --> 테이블 join할 때 필요한 컬럼
# name : 단문
# release_date : 날짜
# num_stars : 숫자
class Album(models.Model):
    artist = models.ForeignKey(
        Musician, on_delete=models.CASCADE
    )  # on_delete=models.CASCADE --> 부모가 제거가 되면 자식도 제거를 하겠다는 의미
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    class Meta:
        db_table = "album"

    def __str__(self) -> str:
        return self.name


# primary_key : 테이블을 생성할 때 하나만 지정가능
#             : unique, not null
# 기본키 필드를 지정하지 않는다면 장고가 기본으로 무조건 생성함
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self) -> str:
        return self.name


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="질문")
    pub_date = models.DateTimeField(verbose_name="작성날짜")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, verbose_name="연결된 질문"
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0, verbose_name="투표")

    def __str__(self):
        return self.choice_text
