from django.contrib.auth.models import BaseUserManager


class AuthentiaUserManager(BaseUserManager):
    def create_user(self, email, **kwargs):
        """
        Creates and saves a generic user with the given email, first_name, surname
        and password.
        """
        if not email:
            raise ValueError('Users must have an email')

        user = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.pop('first_name', ''),
            last_name=kwargs.pop('last_name', ''),
            **kwargs
        )

        password = kwargs.pop('password', '')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(*args, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
