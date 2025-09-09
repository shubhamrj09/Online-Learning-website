'''from django.db import models
from courses.models import Course
from django.contrib.auth.models import User
class UserCourse(models.Model):
    user = models.ForeignKey(User,null= False,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null= False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    enrolled_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.course.name}'
        '''
from django.db import models
from courses.models import Course
from django.contrib.auth.models import User
class UserCourse(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    enrolled_date = models.DateTimeField(auto_now_add=True)  # Automatically set the current date and time when a record is created
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} - {self.course.name}'