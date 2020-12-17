from django.db import models


# Create your models here.

class Stock(models.Model):
    stock_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.stock_name


class Price(models.Model):
    stock_name = models.ForeignKey(Stock, on_delete=models.DO_NOTHING)
    current_price = models.CharField(max_length=264, unique=True)
    max_price = models.CharField(max_length=264, unique=True)
    min_price = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return '{} {} {} {}'.format(self.stock_name, self.current_price, self.max_price, self.min_price)


class DateRecord(models.Model):
    stock_name = models.ForeignKey(Stock, on_delete=models.DO_NOTHING, )
    date = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.stock_name, str(self.date))


class StockCode(models.Model):
    stock_name = models.ForeignKey(Stock, on_delete=models.DO_NOTHING, )
    code = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return '{} {}'.format(self.stock_name, str(self.code))

# Create table out of this run python manage.py migrate
# Then to migrate to an application run python manage.py migration my app
# and then again run python manage.py migrate to apply the changes
