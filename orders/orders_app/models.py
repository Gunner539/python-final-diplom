from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
# from django_rest_passwordreset.tokens import get_token_generator
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

STATE_CHOICES = (
    ('basket', 'Статус корзины'),
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('assembled', 'Собран'),
    ('sent', 'Отправлен'),
    ('delivered', 'Доставлен'),
    ('canceled', 'Отменен'),
)

USER_TYPE_CHOICES = (
    ('shop', 'Магазин'),
    ('buyer', 'Покупатель'),

)