from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField, DateTimeField


class Company(Model):
    ticker = CharField(max_length=20, unique=True)
    name = CharField(max_length=256)
    # industries =


class ReportedEntry(Model):
    company = ForeignKey('Company')
    year = IntegerField()
    name = CharField(max_length=256)
    value = DecimalField(decimal_places=5, max_digits=20)
    statement = CharField(max_length=256, blank=True)
    unique_together = ("company", "year", "name")


class AnalyticEntry(Model):
    company = ForeignKey('Company')
    year = IntegerField()
    name = CharField(max_length=256)
    value = DecimalField(decimal_places=5, max_digits=20)
    type = CharField(max_length=256, blank=True)
    description = CharField(max_length=500,  blank=True)
    unique_together = ("company", "year", "name")


class Stock(Model):
    company = ForeignKey('Company')
    price = DecimalField(decimal_places=5, max_digits=20)