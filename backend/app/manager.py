from django.contrib.auth.models import BaseUserManager
import random

class CustomManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e retorna um usuário com o email e a senha fornecidos.
        """
        if not email:
            raise ValueError(_("O campo email deve ser preenchido."))
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e retorna um superusuário com email e senha fornecidos.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_("Superusuários devem ter is_staff=True."))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_("Superusuários devem ter is_superuser=True."))

        return self.create_user(email, password, **extra_fields)

    # def create_user(self, email, password=None, registrationNumber=None, **extra_fields):

    #     if not email:
    #         raise  ValueError("Invalid e-mail!")
        
    #     regNumber = registrationNumber if registrationNumber else random.randint(1,100000)

    #     email = self.normalize_email(email)
   
    #     user = self.model(
    #         email=email,            
    #         registrationNumber=regNumber,
    #         **extra_fields
    #     )
    #     user.set_password(password)
    #     user.save(using=self.db)
    #     return user
        
    # def create_superuser(self, email, password=None, registrationNumber=None, **extra_fields):
    #     extra_fields.setdefault('is_staff',True)
    #     extra_fields.setdefault('is_superuser',True)
        
    #     return self.create_user(email, password, registrationNumber, **extra_fields)
            
        