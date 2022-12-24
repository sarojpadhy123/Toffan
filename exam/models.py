from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProctorRegistration(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Surname= models.CharField(max_length=100,null=True)
    Full_Name= models.CharField(max_length=100,null=True)
    Fathers_Name = models.CharField(max_length=100,null=True)
    Mothers_Name = models.CharField(max_length=100,null=True)
    Date_of_Birth = models.DateField(null=True)
    Gender = models.CharField(max_length=30,null=True)
    Email_Id = models.EmailField(max_length=150,null=True)
    Contact_No = models.BigIntegerField(null=True)
    ID_PROOF = models.CharField(max_length=30,null=True)
    ID_NO = models.CharField(max_length=30,null=True)
    Degree= models.CharField(max_length=100, null=True)
    If_Other1_Please_Specify= models.CharField(max_length=20, null=True)
    Proctorship_Degree= models.CharField(max_length=100, null=True)
    If_Other2_Please_Specify= models.CharField(max_length=20, null=True)
    Max_Qualification= models.CharField(max_length=20, null=True)
    If_Other3_Please_Specify= models.CharField(max_length=20, null=True)
    Stream= models.CharField(max_length=20, null=True)
    If_Other4_Please_Specify= models.CharField(max_length=50, null=True)
    Honours=models.CharField(max_length=20, null=True)
    If_Other5_Please_Specify= models.CharField(max_length=50, null=True)
    Passed_Out_Year = models.CharField(max_length=50,null=True)
    College_Name=models.CharField(max_length=300, null=True)
    University_Name=models.CharField(max_length=300, null=True)
    Designation=models.CharField(max_length=200, null=True)
    Subject_Questions_Added=models.CharField(max_length=50, null=True)
    Upload_Educational_Certificate=models.ImageField(blank=True, null=True)
    Upload_Proctor_Certificate=models.ImageField(blank=True, null=True)
    Upload_Passport_Size_Photo=models.ImageField(upload_to="my_image",blank=True, null=True)
    Address_Line1=models.CharField(max_length=100, null=True)
    Address_Line2=models.CharField(max_length=100, null=True)
    District=models.CharField(max_length=100, null=True)
    State=models.CharField(max_length=100, null=True)
    Country=models.CharField(max_length=100, null=True)
    Pincode=models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class Add_Course(models.Model):
    Course_Name = models.CharField(max_length=30,null=True)
    Total_Question = models.PositiveIntegerField(null=True)
    Total_Marks = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.Course_Name

class Add_Question(models.Model):
    Course = models.ForeignKey(Add_Course,on_delete=models.CASCADE,null=True)
    Question_Name = models.CharField(max_length=500,null=True)
    Select_Mark = models.PositiveIntegerField(null=True)
    Option1 = models.CharField(max_length=200,null=True)
    Option2 = models.CharField(max_length=200,null=True)
    Option3 = models.CharField(max_length=200,null=True)
    Option4 = models.CharField(max_length=200,null=True)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    Correct_Answer = models.CharField(max_length=100,choices=cat,null=True)

class CandidateRegistration(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Full_Name= models.CharField(max_length=100,null=True)
    Fathers_Name = models.CharField(max_length=100,null=True)
    Mothers_Name = models.CharField(max_length=100,null=True)
    Date_of_Birth = models.DateField(null=True)
    Gender = models.CharField(max_length=30,null=True)
    Contact_No = models.BigIntegerField(null=True)
    ID_PROOF = models.CharField(max_length=30,null=True)
    ID_NO = models.CharField(max_length=30,null=True)
    Email_Id = models.EmailField(max_length=150,null=True)
    Educational_Degree= models.CharField(max_length=100, null=True)
    If_Other1_Please_Specify= models.CharField(max_length=20, null=True)
    Current_Qualification= models.CharField(max_length=20, null=True)
    If_Other2_Please_Specify= models.CharField(max_length=20, null=True)
    Stream= models.CharField(max_length=20, null=True)
    If_Other3_Please_Specify= models.CharField(max_length=50, null=True)
    Honours=models.CharField(max_length=20, null=True)
    If_Other4_Please_Specify= models.CharField(max_length=50, null=True)
    School_Name_or_College_Name = models.CharField(max_length=300, null=True)
    Board=models.CharField(max_length=50, null=True)
    University_Name=models.CharField(max_length=300, null=True)
    Upload_Passport_Size_Photo=models.ImageField(upload_to="my_image",blank=True, null=True)
    Address_Line1=models.CharField(max_length=100, null=True)
    Address_Line2=models.CharField(max_length=100, null=True)
    District=models.CharField(max_length=100, null=True)
    State=models.CharField(max_length=100, null=True)
    Country=models.CharField(max_length=100, null=True)
    Pincode=models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class Sub_Admin_Registration(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Sub_Admin_Name = models.CharField(max_length=100,null=True)
    Mobile_Number = models.BigIntegerField(null=True)
    Email_Id =  models.EmailField(max_length=150,null=True)
    Address = models.CharField(max_length=50,null=True)
    Section = models.CharField(max_length=50,null=True)
    Login_Id = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.user.username
