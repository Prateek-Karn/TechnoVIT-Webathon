from django.db import models

# Create your models here.

# CREATE TABLE Courses (
#   Course_Code varchar PRIMARY KEY,
#   Course_Name varchar NOT NULL,
#   Lecture_hours integer,
#   Tutorial_hours integer,
#   Practical_hours integer,
#   J_Project_hours integer,
#   Credits integer
# );

class Courses(models.Model):
    course_code = models.CharField(primary_key=True, max_length=200)
    course_name = models.CharField(null=False, max_length=200)
    lecture_hours = models.IntegerField(null=True)
    tutorial_hours = models.IntegerField(null=True)
    practical_hours = models.IntegerField(null=True)
    j_proj_hours = models.IntegerField(null=True)
    credits = models.IntegerField(null=True)

    def __str__(self):
        return self.course_name

# CREATE TABLE Wishlist(
#   Course_Code varchar PRIMARY KEY,
#   Course_Name varchar NOT NULL,
#   No_of_Wishlist_received integer
# );

class Wishlist(models.Model):
    course_code = models.CharField(primary_key=True, max_length=200)
    course_name = models.CharField(null=False, max_length=200)
    no_of_wishlist_recieved = models.IntegerField(null=True)

    def __str__(self):
        return self.course_name

# CREATE TABLE Faculty(
#   Sl_no integer,
#   Emp_id integer PRIMARY KEY,
#   Name varchar NOT NULL,
#   Designation varchar NOT NULL,
#   Phno integer UNIQUE,
#   School varchar,
#   Email varchar
# );


class Faculty(models.Model):
    sl_no = models.AutoField(primary_key=True)
    emp_id = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=200)
    designation = models.CharField(null=False, max_length=200)
    phone_number = models.IntegerField()
    school = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# CREATE TABLE Preferences (
#   Sl_no integer,
#   Emp_id integer PRIMARY KEY,
#   Name varchar NOT NULL,
#   Designation varchar NOT NULL,
#   p1 varchar NOT NULL,
#   p2 varchar NOT NULL,
#   p3 varchar NOT NULL,
#   p4 varchar NOT NULL,
#   p5 varchar NOT NULL,
#   a1 varchar,
#   a2 varchar
# );
class Preferences(models.Model):
    sl_no = models.IntegerField()
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    p1 = models.CharField(max_length=200)
    p2 = models.CharField(max_length=200)
    p3 = models.CharField(max_length=200)
    p4 = models.CharField(max_length=200)
    p5 = models.CharField(max_length=200)
    a1 = models.CharField(max_length=200,null=True)
    a2 = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name


# CREATE TABLE Batch (
#   Course_Code varchar PRIMARY KEY,
#   No_of_batches integer,
#   After_prof integer
# );

class Batch(models.Model):
    course_code = models.CharField(primary_key=True, max_length=200)
    no_of_batches = models.IntegerField()
    after_prof = models.IntegerField(null=True)

    def __str__(self):
        return self.course_code