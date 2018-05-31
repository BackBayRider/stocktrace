#-*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone
from datetime import datetime, date
from django.conf import settings
from mongoengine import Document

db = settings.DB


class Portfolio(Document):
    # static variable here
    position_ratio_limit = 90

    def __init__(self, stocks, name=None):
        if name:
            self.name = name
        else:
            self.name = str(date.today())
        self.stocks = stocks
        # 三个账户当年本金
        self.cost = 493000+218579+277461
        # 融资
        self.financing = 200000
        # 市值
        self.market_value = 0
        # 总资产
        self.total = 0
        # 现金
        self.cash = 0
        # 净资产
        self.net_asset = 0
        # 盈利
        self.profit = 0
        # 盈利率
        self.profit_ratio = 0
        # 当日盈利
        self.profit_today = 0
        # 当日盈利%
        self.profit_ratio_today = 0

        for stock in self.stocks:
            try:
                if stock['code'] == '131810':
                    self.cash += float(stock['amount'])
                else:
                    value = float(stock['amount'])*float(stock['current'])
                    self.market_value += value
                    self.profit_today += float(stock['amount'])*float(stock['change'])
            except KeyError as e:
                pass
        self.total += self.market_value+self.cash
        self.net_asset = self.total - self.financing

        # 仓位
        self.position_ratio = 0
        # 杠杆
        self.lever = 0
       
        if self.total != 0:
            self.position_ratio = self.market_value/self.total
            self.lever = self.total/self.net_asset
            # 个股占比
            for stock in self.stocks:
                try:
                    if stock['code'] == '131810':
                        stock['ratio'] = float(stock['amount'])/self.total
                        stock['market'] = float(stock['amount'])
                    else:
                        value = float(stock['amount']) * float(stock['current'])
                        stock['ratio'] = value / self.total
                        stock['market'] = value
                except KeyError as e:
                    pass
        self.profit = self.net_asset - self.cost
        self.profit_ratio = (self.net_asset-self.cost)/self.cost
        self.profit_ratio_today = self.profit_today/self.net_asset
        self.date = datetime.now()

    def save(self):
        stock_list = []
        for stock in self.stocks:
            stock_list.append({'code': stock['code'], 'amount': stock['amount'], 'current': stock['current']})
        db.portfolio.insert({'name':self.name, 'date': self.date, 'stocks': stock_list,
                             'market_value': self.market_value,
                             'total': self.total, 'net_asset': self.net_asset,'financing': self.financing,
                             'position_ratio': self.position_ratio, 'profit_ratio': self.profit_ratio})

    def __unicode__(self):
        return self.name
