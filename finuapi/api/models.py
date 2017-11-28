from django.db.models import Model, CharField, ForeignKey, IntegerField, DecimalField


class Company(Model):
    ticker = CharField(max_length=20)
    name = CharField(max_length=256)
    # industries =


class StatementEntry(Model):
    company = ForeignKey('Company')
    year = IntegerField(primary_key=True)
    name = CharField(max_length=256, primary_key=True)
    value = DecimalField()
    statement = CharField(max_length=256)


class AnalyticEntry(Model):
    company = ForeignKey('Company', primary_key=True)
    year = IntegerField(primary_key=True)
    name = CharField(max_length=256, primary_key=True)
    value = DecimalField()
    type = CharField(max_length=256)
    description = CharField(max_length=500)


class Stock(Model):
    ticker = ForeignKey('Company', primary_key=True)
    price = DecimalField()
    # date = Column(DateTime())