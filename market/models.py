from django.db import models
from mongoengine import *


# Create your models here.
class Market(Document):
    name = StringField()
    total_market_cap = FloatField()
    volume = FloatField()
    turnover = FloatField()
    pe = FloatField()
    value = FloatField()
    date = DateTimeField()
    # '''
    # classdocs
    # '''
    #
    # def __init__(self, name, total_market_cap, volume, turnover, pe, value=0, date=None):
    #     self.name = name
    #     try:
    #         self.total_market_cap = float(total_market_cap)
    #     except TypeError:
    #         self.total_market_cap = 0
    #
    #     try:
    #         self.volume = float(volume)
    #     except TypeError:
    #         self.volume = 0
    #
    #     try:
    #         self.turnover = float(turnover)
    #     except TypeError:
    #         self.turnover = 0
    #
    #     try:
    #         self.pe = float(pe)
    #     except TypeError:
    #         self.pe = 0
    #
    #     try:
    #         self.value = float(value)
    #     except TypeError:
    #         self.value = 0
    #
    #     self.date = date
    #
    #     '''
    #     Constructor
    #     '''

    def __str__(self):
        return '{} market:{} volume:{} turnover:{} PE:{} Index:{} Date:{}'.format(self.name,
                                                                                  self.total_market_cap,
                                                                                  self.volume, self.turnover,
                                                                                  self.pe, self.value,
                                                                                  self.date)
