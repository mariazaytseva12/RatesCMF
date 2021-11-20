#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[144]:


def DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm):
    coup_cash = coupon_annual * coup_freq * notional
    remain = years_exp - as_of
    numb_periods = int(remain // coup_freq)
    first_coup = remain - coup_freq * numb_periods
    sum = 0
    for i in range(numb_periods):
        time = first_coup + i * coup_freq
        discount = (1 / (1 + ytm * coup_freq) ** (i + 1))
        cash_disc = coup_cash * discount
        sum = sum + cash_disc
    discount_last = (1 / (1 + ytm * coup_freq) ** (numb_periods))
    dirty_price = sum + notional * discount_last
    return dirty_price


# In[145]:


DirtyCouponBondPrice(years_exp=4, as_of=1.1, coup_freq=1, coupon_annual=0.1, notional=100, ytm=0.2)


# In[146]:


def AccuredInterest(years_exp, as_of, coup_freq, coupon_annual, notional, ytm):
    coup_cash = coupon_annual * coup_freq * notional
    remain = years_exp - as_of
    numb_periods = int(remain // coup_freq)
    first_coup = remain - coup_freq * numb_periods + coup_freq
    accrual_period = coup_freq - first_coup
    ai = coup_cash * accrual_period
    discount = (1 / (1 + ytm * coup_freq) ** (-accrual_period))
    dai = ai * discount
    return dai


# In[147]:


AccuredInterest(years_exp=4, as_of=2, coup_freq=1, coupon_annual=0.1, notional=100, ytm=0.2)


# In[148]:


def CleanCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm):
    Price = DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm) 
    - AccuredInterest(years_exp, as_of, coup_freq, coupon_annual, notional, ytm)
    return Price


# In[149]:


CleanCouponBondPrice(years_exp=4, as_of=2, coup_freq=1, coupon_annual=0.1, notional=100, ytm=0.2)


# In[150]:


def Duration(years_exp, as_of, coup_freq, coupon_annual, notional, ytm):
    coup_cash = coupon_annual * coup_freq * notional
    remain = years_exp - as_of
    numb_periods = int(remain // coup_freq)
    first_coup = remain - coup_freq * numb_periods
    sum = 0
    for i in range(numb_periods):
        time = first_coup + i * coup_freq
        discount = (1 / (1 + ytm * coup_freq) ** (i + 1))
        cash_disc = coup_cash * discount * (i + 1)
        sum = sum + cash_disc
    discount_last = (1 / (1 + ytm * coup_freq) ** (numb_periods))
    Summa = sum + notional * discount_last * (i + 1)
    MacD = Summa / DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm) * coup_freq
    ModD = MacD / (1 + ytm)
    return ModD


# In[151]:


Duration(years_exp=4, as_of=2, coup_freq=1, coupon_annual=0.1, notional=100, ytm=0.2)


# In[152]:


def DV01(years_exp, as_of, coup_freq, coupon_annual, notional, ytm):
    Dv = Duration(years_exp, as_of, coup_freq, coupon_annual, notional, ytm) * DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm) / 100
    return Dv


# In[153]:


DV01(years_exp=4, as_of=2, coup_freq=1, coupon_annual=0.1, notional=100, ytm=0.2)


# In[154]:


def ConvexityApprox(years_exp, as_of, coup_freq, coupon_annual, notional, ytm, ytm_change):
    price0 = DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm)
    price_pos = DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm + ytm_change)
    price_neg = DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm - ytm_change)
    conv = (price_neg + price_pos - 2 * price0) / (2 * price0 * (ytm_change)**2)
    return conv


# In[155]:


ConvexityApprox(years_exp=4, as_of=2, coup_freq=1, coupon_annual=0.1, notional=100, ytm=0.2, ytm_change=0.01)


# In[161]:


def Rolldown(years_exp, as_of, coup_freq, coupon_annual, notional, ytm, time_change):
    price0 = DirtyCouponBondPrice(years_exp, as_of, coup_freq, coupon_annual, notional, ytm)
    price_pos = DirtyCouponBondPrice(years_exp, as_of + time_change, coup_freq, coupon_annual, notional, ytm)
    rd = (price_pos - price0)
    return rd


# In[170]:


Rolldown(years_exp = 4, as_of = 2, coup_freq = 1, coupon_annual = 0.1, notional = 100, ytm = 0.2, time_change = 1)


# In[ ]:




