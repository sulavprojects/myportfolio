from django.db import models




# Create your models here.

class Update(models.Model):
    title = models.CharField(max_length=25, default='sulav pariyar portfolio')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    first_auto = models.CharField(max_length=50)
    second_auto = models.CharField(max_length=50)
    second_auto = models.CharField(max_length=50)
    my_short_discription = models.TextField(max_length=500)
    my_cv = models.FileField(upload_to="mycv")
    profilepic = models.ImageField(upload_to="profilepic")
    About_me_description = models.TextField(max_length=1000)
    DOB = models.DateField()
    freelancer = models.CharField(max_length=10)
    adderss = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    nationality = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()


    def __str__(self):
        return self.title




class Services(models.Model):
    first_service_title = models.CharField(max_length=25)
    first_service_Discription = models.TextField()

    second_service_title = models.CharField(max_length=25)
    second_service_Discription = models.TextField()

    third_service_title = models.CharField(max_length=25)
    third_service_Discription = models.TextField()

    fourth_service_title = models.CharField(max_length=25)
    fourth_service_Discription = models.TextField()

    fifth_service_title = models.CharField(max_length=25)
    ffith_service_Discription = models.TextField()

    sixth_service_title = models.CharField(max_length=25)
    sixth_service_Discription = models.TextField()


    def __str__(self):
        return self.first_service_title + ' - ' + self.second_service_title + ' - ' + self.third_service_title + ' - ' + self.fourth_service_title + ' - ' + self.fifth_service_title + ' - ' + self.sixth_service_title


class Expreance(models.Model):

    workyear = models.CharField(max_length=100)
    workas = models.CharField(max_length=100)
    work_discription = models.TextField(max_length=100)

    def __str__(self):
        return self.workyear


class Education(models.Model):

    studyyear = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    study_discription = models.TextField(max_length=100)

    def __str__(self):
        return self.studyyear


class Myskills(models.Model):
    skill_name = models.CharField(max_length=25)

    def __str__(self):
        return self.skill_name


class Funfact(models.Model):
    nameone_title = models.CharField(max_length=20)
    nameone = models.IntegerField()

    nametwo_title = models.CharField(max_length=20)
    nametwo = models.IntegerField()

    namethree_title = models.CharField(max_length=20)
    namethree = models.IntegerField()

    namefour_title = models.CharField(max_length=20)
    namefour = models.IntegerField()








