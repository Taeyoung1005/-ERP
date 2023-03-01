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
    
class HR(models.Model):
    사번 = models.IntegerField(primary_key=True)
    구분 = models.CharField(max_length=20, default='', null=True, blank=True)
    이름 = models.CharField(max_length=20, default='', null=True, blank=True)
    영문이름 = models.CharField(max_length=20, default='', null=True, blank=True)
    근무지 = models.CharField(max_length=20, default='', null=True, blank=True)
    부서 = models.CharField(max_length=20, default='', null=True, blank=True)
    팀 = models.CharField(max_length=20, default='', null=True, blank=True)
    직급 = models.CharField(max_length=20, default='', null=True, blank=True)
    직책 = models.CharField(max_length=30, default='', null=True, blank=True)
    입사일 = models.DateField(default='', null=True, blank=True)
    근속일 = models.IntegerField(default='', null=True, blank=True)
    주민등록번호 = models.CharField(max_length=20, default='', null=True, blank=True)
    생년월일 = models.DateField(default='', null=True, blank=True)
    연락처 = models.CharField(max_length=20, default='', null=True, blank=True)
    비상연락망 = models.CharField(max_length=20, default='', null=True, blank=True)
    회사이메일 = models.CharField(max_length=100, default='', null=True, blank=True)
    개인이메일 = models.CharField(max_length=100, default='', null=True, blank=True)
    주소 = models.CharField(max_length=70, default='', null=True, blank=True)
    최종학력 = models.CharField(max_length=20, default='', null=True, blank=True)
    학위 = models.CharField(max_length=20, default='', null=True, blank=True)
    학교 = models.CharField(max_length=20, default='', null=True, blank=True)
    전공 = models.CharField(max_length=20, default='', null=True, blank=True)
    학점 = models.CharField(max_length=20, default='', null=True, blank=True)
    입사구분 = models.CharField(max_length=20, default='', null=True, blank=True)
    경력사항1 = models.CharField(max_length=20, default='', null=True, blank=True)
    경력사항2 = models.CharField(max_length=20, default='', null=True, blank=True)
    경력사항3 = models.CharField(max_length=20, default='', null=True, blank=True)
    경력사항4 = models.CharField(max_length=20, default='', null=True, blank=True)
    경력사항5 = models.CharField(max_length=20, default='', null=True, blank=True)
    자격사항1 = models.CharField(max_length=20, default='', null=True, blank=True)
    자격사항2 = models.CharField(max_length=20, default='', null=True, blank=True)
    자격사항3 = models.CharField(max_length=20, default='', null=True, blank=True)
    자격사항4 = models.CharField(max_length=20, default='', null=True, blank=True)
    자격사항5 = models.CharField(max_length=20, default='', null=True, blank=True)
    어학사항1 = models.CharField(max_length=20, default='', null=True, blank=True)
    어학사항2 = models.CharField(max_length=20, default='', null=True, blank=True)
    어학사항3 = models.CharField(max_length=20, default='', null=True, blank=True)
    어학사항4 = models.CharField(max_length=20, default='', null=True, blank=True)
    어학사항5 = models.CharField(max_length=20, default='', null=True, blank=True)
    is_activate = models.BooleanField(default=True)

    class Meta:
        managed = True
        ordering = ['사번']
        db_table = 'api_hr'