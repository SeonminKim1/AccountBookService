from django.db import models
from user.models import User
# from accountbook.models import AccountBookType

class Category(models.Model):
    account_book_type = models.ForeignKey(
        to = 'accountbook.AccountBookType', 
        on_delete=models.CASCADE, 
        verbose_name='AccountBook Type in Category',
    )
    writer = models.ForeignKey(
        to = User,
        on_delete=models.SET_NULL, 
        null=True,
        verbose_name='Category Writer',
    )
    name = models.CharField(
        max_length=30,
        blank=False,
        verbose_name='Category name',
    )
    is_custom = models.BooleanField(
        default=False,
        verbose_name='Custom check',
    )

    def __str__(self):
        return f'{self.writer} - {self.account_book_type} - {self.name}'

    class Meta:
        db_table = "CATEGORY"

