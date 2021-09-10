from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from courses.models import Courses
from cal.models import Event

class StudentSerializer(serializers.ModelSerializer):
      class Meta:
            model= Student
            fields=("first_name","last_name","age","nationality","gender","language","date_of_enrolment","phone_number")


class TeacherSerializer(serializers.ModelSerializer):
      class Meta:
            model= Teacher
            fields=("first_name","last_name","age","nationality","email","phone_number","gender","languages","date_hired","course")


class CoursesSerializer(serializers.ModelSerializer):
      class Meta:
            model= Courses
            fields=("course_name","course_code","syllabus","course_duration","course_instractor")
     

class EventSerializer(serializers.ModelSerializer):
      class Meta:
            model= Event
            fields=("title","description","start_time","end_time")
     