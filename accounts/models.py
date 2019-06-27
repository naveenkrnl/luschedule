from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator
# from .utils import code_generator
# Create your models here.

BRANCH_CHOICES = (
    ("CSE", "B.Tech.- Comp. Sc. & Engg."),
    ("ELECCOMM", "B.Tech.- Elec. & Comm. Engg."),
    ("MECHANICAL", "B.Tech.- Mechanical Engg."),
    ("ELECTRICAL", "B.Tech.- Electrical Engg."),
    ("IT", "B.Tech.- Information Technology"),
    ("BBA", "BBA"),
    ("BCA", "BCA"),
    ("MBA", "MBA"),
    ("MCA", "MCA"),
    ("MCSE", "M.Tech.- Comp. Sc. & Engg."),
    ("MELECCOMM", "M.Tech.- Elec. & Comm. Engg."),
)
SEMESTER_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username, 
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

USERNAME_REGEX='^[a-zA-Z0-9.@+-]*$'
ROLLNO_REGEX='^[0-9]*$'


class MyUser(AbstractBaseUser):
    username=models.CharField(max_length=120,validators=[RegexValidator(
        regex=USERNAME_REGEX,
        message="Username must be alphanumeric",
        code='invalid_username'
        )],
        unique=True,
    )
    name=models.CharField(max_length=120)
    rollno=models.CharField(max_length=120,validators=[RegexValidator(
        regex=ROLLNO_REGEX,
        message="Sahi Roll Number Daalo !!",
        code='invalid_rollno'
        )],
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    branch=models.CharField(max_length=200, choices=BRANCH_CHOICES,default='CSE')
    semester=models.CharField(max_length=200,choices=SEMESTER_CHOICES,default='6')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin

# class ActivationProfile(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     key=models.CharField(max_length=255)
#     expired=models.BooleanField(default=False)

#     def save(self, *args, **kwargs):
#         self.key=code_generator() 
#         super(ActivationProfile,self).save(*args, **kwargs)
# def post_save_activation_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             print('Activation Created')
#         except:
#             pass
# post_save.connect(post_save_activation_receiver, sender=ActivationProfile)


class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=None)
    profilepic=models.ImageField(upload_to='profilepics')


    def __str__(self):
        return str(self.user.username)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            new_profile = Profile.objects.get_or_create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
