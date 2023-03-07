from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserManager(BaseUserManager):
    def _create_user(self, email, password, name, nickname, **extra_fields):
        """
        Create and save a user with the given email, password, name.
        """
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, name=name, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, name, nickname, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, name, nickname, **extra_fields)

    def create_superuser(self, email, password, name, nickname=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, name, nickname, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User 생성 : AbstractUser or AbstractBaseUser 상속
    필드 추가 : username, password, name, phone

    권한 여부 추가
    """

    # null = True 지정하지 않으면 not null + unique ==> pk 속성
    email = models.CharField(verbose_name="이메일", max_length=255, unique=True)
    password = models.CharField(verbose_name="비밀번호", max_length=128)
    name = models.CharField(verbose_name="이름", max_length=64)
    nickname = models.CharField(verbose_name="별명", max_length=50)
    is_staff = models.BooleanField(verbose_name="관리자여부", default=False)

    # CustomUser 를 기반으로 user 생성을 도와줄 매니저 클래스 등록
    objects = UserManager()  # User.objects.create_user() 생성

    # email(아이디) 으로 사용할 필드 지정
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name", "nickname"]

    def __str__(self) -> str:
        return "<%d %s>" % (self.pk, self.email)


class Profile(models.Model):
    """
    회원가입 시 무조건 같이 실행
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="회원")
    image = models.ImageField(
        upload_to="profile/", default="profile/default.png", verbose_name="프로필 이미지"
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
