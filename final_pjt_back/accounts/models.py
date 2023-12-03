from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **ex):
        if not email:
            raise ValueError('Email을 입력해주세요.')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **ex)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **ex):
        ex.setdefault('is_active', True)
        ex.setdefault('is_staff', False)
        ex.setdefault('is_superuser', False)
        return self._create_user(email, password, **ex)

    
    def create_superuser(self, username, email, password, **ex):
        ex.setdefault('is_active', True)
        ex.setdefault('is_staff', True)
        ex.setdefault('is_superuser', True)   
        return self._create_user(username, email, password, **ex)
    

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        email = data.get("email")
        username = data.get("username")
        birth = data.get("birth")
        money = data.get("money")
        salary = data.get("salary")
        product = data.get("products")
        married = data.get("married")
        main_bank = data.get("main_bank")
        save_type = data.get("save_type")
        phone = data.get("phone")
        address = data.get("address")
        user_email(user, email)
        user_username(user, username)
        if phone:
            user.phone = phone
        if address:
            user.address = address
        if birth:
            user.birth = birth
        if money:
            user.money = money
        if salary:
            user.salary = salary
        if product:
            products = user.product.split(',')
            products.append(product)
            if len(products) > 1:
                products = ','.join(products)
            user_field(user, "products", products)
        if married:
            user.married = married
        if main_bank:
            user.main_bank = main_bank
        if save_type:
            user.save_type = save_type
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
            


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)                                  # Email
    username = models.CharField(max_length=30, unique=False)                # 이름
    birth = models.DateField(blank=True, null=True)                         # 나이
    phone = models.CharField(max_length=20)                                 # 전화번호
    address = models.CharField(max_length=100)                              # 주소
    products = models.CharField(max_length=200, blank=True, default='')     # 가입상품
    money = models.IntegerField(blank=True, null=True)                      # 자산
    salary = models.IntegerField(blank=True, null=True)                     # 연봉
    married = models.BooleanField(blank=True, null=True, default=False)                    # 결혼여부
    main_bank = models.CharField(max_length=20)                             # 주거래은행
    save_type = models.IntegerField(blank=True, null=True)                  # 저축 타입(1:, 2: , 3:, 4: ) 
    
    objects = UserManager()
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['username']