from django.db import models
from user.models import User
from category.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator

ACCOUNT_BOOK_TYPE = (
        ("Expenditure", "지출"), ("Income", "수입"),
)   

ACCOUNT_BOOK_PRICE_RANGE = (0, 4294967294)

class AccountBookType(models.Model):
    name = models.CharField(
        choices = ACCOUNT_BOOK_TYPE, 
        max_length=25,
        verbose_name='AccountBookType name',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ACCOUNT_BOOK_TYPE"

class AccountBook(models.Model):
    account_book_type = models.ForeignKey(
        to = AccountBookType, 
        on_delete=models.CASCADE, 
        verbose_name='AccountBook Type',
    )
    recorder = models.ForeignKey(
        to = User,
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='AccountBook Recorder',
    )
    category = models.ForeignKey(
        to = Category, 
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='AccountBook Category',
    )
    # Positive Integer = mysql unsigned int (0~42억)
    price = models.PositiveIntegerField( 
        validators=[
            MinValueValidator(ACCOUNT_BOOK_PRICE_RANGE[0]),
            MaxValueValidator(ACCOUNT_BOOK_PRICE_RANGE[1]),
        ], 
        default=0,
        verbose_name='AccountBook Price',
        help_text='Price is only a positive number greater than 0',
    )
    dt = models.DateTimeField(
        auto_now=True,
        verbose_name='AccountBook Time',
    )
    memo = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='AccountBook Memo',
    )
    is_satisfied = models.BooleanField(
        default=False,
        verbose_name='Satisfaction Check',
        help_text='If you satisfied true, otherwise false'
    )

    def __str__(self):
        return f'{self.recorder} - {self.account_book_type} - {self.price}'

    class Meta:
        db_table = "ACCOUNT_BOOK"
