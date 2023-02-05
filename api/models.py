from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class coa(models.Model):
    코드 = models.IntegerField(default='', primary_key=True)
    계정명 = models.CharField(max_length=20, blank=True, default='', null=True)
    계정_대분류 = models.CharField(max_length=20, blank=True, default='', null=True)
    계정_중분류 = models.CharField(max_length=20, blank=True, default='', null=True)
    계정_소분류 = models.CharField(max_length=20, blank=True, default='', null=True)
    재무제표 = models.CharField(max_length=20, blank=True, default='', null=True)
    비고 = models.CharField(max_length=100, blank=True, default='', null=True)

    class Meta:
        managed = True
        ordering = ['코드']
        db_table = 'api_coa'

class product(models.Model):
    제품코드 = models.IntegerField(default='', primary_key=True)
    제품명 = models.CharField(max_length=20, blank=True, default='', null=True)
    포장단위 = models.CharField(max_length=20, blank=True, default='', null=True)
    제약사 = models.CharField(max_length=20, blank=True, default='', null=True)
    보험코드 = models.CharField(max_length=20, blank=True, default='', null=True)
    표준코드 = models.CharField(max_length=20, blank=True, default='', null=True)
    기준가 = models.CharField(max_length=20, blank=True, default='', null=True)
    급여 = models.CharField(max_length=20, blank=True, default='', null=True)
    구분 = models.CharField(max_length=20, blank=True, default='', null=True)
    성분코드 = models.CharField(max_length=20, blank=True, default='', null=True)

    class Meta:
        managed = True
        ordering = ['제품코드']
        db_table = 'api_product'

class UserManager(BaseUserManager):
    def create_user(self, email, nickname, name, password=None):
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        if not name:
            raise ValueError('must have user name')
        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            name = name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, nickname, name, password=None):
        user = self.create_user(
            email,
            password = password,
            nickname = nickname,
            name = name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(default='', max_length=100, null=False, blank=False)
    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'nickname'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'name']

    def __str__(self):
        return self.nickname