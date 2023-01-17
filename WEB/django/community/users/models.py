from django.db import models

# Create your models here.


from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
    UserManager,
)

# User 객체
# 속성 -  username, password, email, first_name, last_name

# AbstractUser
# AbstractBaseUser 상속
# username, first_name, last_name, email
# is_staff, is_active, date_joined

# AbstractBaseUser
# password, last_login, is_active

# 프로젝트에서 필요한 User
# email 필드 id개념 username
# gender 필요 수요 아님
# password
# name 필수


class UserManger(BaseUserManager):
    def _create_user(self, email, password, name, phone, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, name, phone, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, name, phone, **extra_fields)

    def create_superuser(self, email, password, name, **extra_fields):
        """
        성별은 입력 필요 없은 어드민 일때 
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, name, phone=None, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User 생성 : AbstractUser 상속 or AbstractBaseUser
    필두 추가 : email, gender, name 
    
    권한 여부 
    """

    # null=True 지정하지 않으면 not NULL, + unique ==> pk속성
    email = models.EmailField(verbose_name="이메일", max_length=255, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=128)
    name = models.CharField(verbose_name="이름", max_length=64)
    # phone 비어 있거나 널 허용
    phone = models.CharField(verbose_name="핸드폰", max_length=50, blank=True, null=True)

    is_staff = models.BooleanField(verbose_name="관리자여부", default=False)

    # CustomUser 를 기반으로 user 생성을 도와줄 매니저 클래스 등록

    object = UserManger()
    # username으로 사용할 필드 지정
    USERNAME_FIELD = "email"

    # email, password 요소 외에 사용자  생성 시 꼭 받아야 하는 필드 작성
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return "%s" % (self.email)
