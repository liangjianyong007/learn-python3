# -*- coding: utf-8 -*-
# p:previous 上一个
# m：month 月
# y：year 年
# c:current 当前
# l：last 最后
# n：next 下一个
# w：week 周
# f：fisrt 第一  如：cwf 当前周第一天
# f在首位：Finance 财年 如：fyf财年第一天
import datetime
import calendar
import re
class DateFuncUtils(object):
    def evaluate(self, str, fmt):
        express = re.compile(r'^\d{8}$')
        match = express.match(str)
        if match:
                dt = datetime.datetime.strptime(str, "%Y%m%d")
                switch_dict = {
                    #当前周第一天
                    "cwf": dt + datetime.timedelta(days=-dt.weekday()),
                    #本周最后一天
                    "cwl": dt + datetime.timedelta(days=6-dt.weekday()),
                    #上周第一天
                    "pwf": dt + datetime.timedelta(days=-dt.weekday())+ datetime.timedelta(days=-7),
                    #上周最后一天
                    "pwl": dt + datetime.timedelta(days=-dt.weekday())+ datetime.timedelta(days=-1),
                    #下周第一天
                    "nwf": dt + datetime.timedelta(days=7-dt.weekday()) ,
                    #下周最后一天
                    "nwl": dt + datetime.timedelta(days=6-dt.weekday()) + datetime.timedelta(days=7),
                    #当月第一天
                    "cmf": dt.replace(day=1),
                    #当月最后一天
                    "cml": datetime.date(year=dt.year, month=dt.month, day=calendar.monthrange(dt.year, dt.month)[1]),
                    #上个月第一天
                    "pmf": datetime.date(year=dt.year-1, month=12, day=1) if dt.month == 1 else datetime.date(year=dt.year, month=dt.month-1, day=1),
                    #上个月最后一天
                    "pml": datetime.date(year=dt.year-1, month=12, day=31) if dt.month == 1 else datetime.date(year=dt.year, month=dt.month-1, day=calendar.monthrange(dt.year, dt.month-1)[1]),
                    #下一个月第一天
                    "nmf": datetime.date(year=dt.year+1, month=1, day=1) if dt.month == 12 else datetime.date(year=dt.year, month=dt.month+1, day=1),
                    #下一个月最后一天
                    "nml": datetime.date(year=dt.year+1, month=1, day=calendar.monthrange(dt.year, dt.month)[1]) if dt.month == 12 else datetime.date(year=dt.year, month=dt.month+1, day=calendar.monthrange(dt.year, dt.month+1)[1]),
                    #当前季度第一天
                    "cqf": datetime.date(year=dt.year, month=(int((dt.month-1)/3)*3+1), day=1),
                    #当前季度最后一天
                    "cql": datetime.date(year=dt.year, month=int((dt.month+2)/3)*3, day=calendar.monthrange(dt.year, int((dt.month+2)/3)*3)[1]),
                    #上一个季度的第一天
                    "pqf": datetime.datetime((datetime.date(year=dt.year, month=(int((dt.month-1)/3)*3+1), day=1) - datetime.timedelta(days=1)).year, month=(datetime.date(year=dt.year, month=(int((dt.month-1)/3)*3+1), day=1) - datetime.timedelta(days=1)).month - 2, day=1),
                    #上一个季度的最后一天
                    "pql":datetime.datetime(dt.year, (dt.month - 1) - (dt.month - 1) % 3 + 1, 1) - datetime.timedelta(days=1),
                    #本年第一天
                    "cyf": datetime.date(year=dt.year, month=1, day=1),
                    #本年最后一天
                    "cyl": datetime.date(year=dt.year, month=12, day=31),
                    #上一年第一天
                    "pyf": datetime.date(year=dt.year-1, month=1, day=1),
                    #下一年最后一天
                    "nyl": datetime.date(year=dt.year+1, month=12, day=31),
                    #本财年第一天
                    "fyf": datetime.date(year=dt.year, month=4, day=1),
                    #本财年最后一天
                    "fyl": datetime.date(year=dt.year+1, month=3, day=31),
                    #上一财年第一天
                    "fyp": datetime.date(year=dt.year-1, month=4, day=1),
                    #下一财年最后一天
                    "fyn": datetime.date(year=dt.year+1, month=3, day=31)
                }
                return switch_dict.get(fmt).strftime("%Y%m%d")

u=DateFuncUtils()
print(u.evaluate("20180216", "fyf"))