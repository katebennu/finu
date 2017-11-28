from django.db.models import Model, CharField, ForeignKey, OneToOneField, IntegerField, DecimalField


class Company(Model):
    ticker = CharField(max_length=20)
    name = CharField(max_length=256)
    # industries =


class StatementEntry(Model):
    company = ForeignKey('Company')
    year = IntegerField()
    name = CharField(max_length=256)
    value = DecimalField(decimal_places=5, max_digits=20)
    statement = CharField(max_length=256)


class AnalyticEntry(Model):
    company = ForeignKey('Company')
    year = IntegerField()
    name = CharField(max_length=256)
    value = DecimalField(decimal_places=5, max_digits=20)
    type = CharField(max_length=256)
    description = CharField(max_length=500)


class Stock(Model):
    ticker = ForeignKey('Company')
    price = DecimalField(decimal_places=5, max_digits=20)
    # date = Column(DateTime())