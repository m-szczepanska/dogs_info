from datetime import datetime, timezone

from uuid import uuid4

from django.contrib.auth.hashers import check_password, make_password
from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(BaseModel):
    """ Model containing four basic informations from users to login.
    Args:
        login - string; max length 50 chars
        email - unique string; max length 254 chars
        _password - hashed string
    """
    login = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=254, blank=False, unique=True)
    _password = models.CharField(max_length=255, blank=False)  # hashed

    def check_password(self, password_plaintext):
        return check_password(password_plaintext, self._password)

    # TODO: Add validation when creating user
    def set_password(self, password_plaintext) -> None:
        password_hashed = make_password(password_plaintext)
        self._password = password_hashed
        self.save()


class Token(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=200, default=uuid4)
    is_expired = models.BooleanField(default=False)


class CreateAccountToken(BaseModel):
    email = models.EmailField(max_length=254)
    uuid = models.CharField(max_length=200, default=uuid4)
    was_used = models.BooleanField(default=False)

    @property
    def is_valid(self) -> bool:
        timedelta = datetime.now(timezone.utc) - self.created_at
        return not self.was_used and timedelta.days < 1


class PasswordResetToken(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=200, default=uuid4)
    was_used = models.BooleanField(default=False)

    @property
    def is_valid(self) -> bool:
        timedelta = datetime.now(timezone.utc) - self.created_at
        return not self.was_used and timedelta.days < 1