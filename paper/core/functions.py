#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
import time
import pandas as pd


# In[2]:


def diff_day(t1, t2):
    dt1 = datetime.utcfromtimestamp(t1)
    dt2 = datetime.utcfromtimestamp(t2)
    return (dt2 - dt1).days


# In[3]:


# [最晚输入与最早输出天数之差, 生命周期, 活动天数, 每日最大交易次数, 传入时间的区间长度, 传出时间的区间长度]


# In[4]:


def analysize_timestamps(ts0, ts1, ts2):
    result = []
    result.append(diff_day(max(ts1), min(ts2)))

    _all = ts1 + ts2
    _all.sort()
    result.append(diff_day(_all[0], _all[-1]))

    day = lambda ts : datetime.utcfromtimestamp(ts).date()
    days = [day(ts) for ts in _all]
    day_num = pd.value_counts(days)
    for ts in ts0:
        day_num[day(ts)] -= 1
    result.append(len(day_num))
    result.append(day_num.max())

    result.append(diff_day(min(ts1), max(ts1)))
    result.append(diff_day(min(ts2), max(ts2)))

    return result

