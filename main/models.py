from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.IntegerField()
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.question

class ScoreBoard(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s score for {self.course.course_name}: {self.score}"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')
    whatsapp_link = models.URLField()

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class QuestionbankCourse(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class QuestionbankQuestion(models.Model):
    Questionbank_course = models.ForeignKey(QuestionbankCourse, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.IntegerField()
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)
    marks = models.IntegerField(default=1)

    def __str__(self):
        return self.question

class QuestionbankScoreBoard(models.Model):
    Questionbankcourse = models.ForeignKey(QuestionbankCourse, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

   

class MedicalCourse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    duration_months = models.IntegerField()
    seats_available = models.IntegerField()
    team_members = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


class CACourse(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    duration_months = models.IntegerField()
    seats_available = models.IntegerField()
    team_members = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)

    def __str__(self):
      if self.user.username:
        return self.user.username
      else:
        return f"Profile of {self.user}"  # Fallback message


