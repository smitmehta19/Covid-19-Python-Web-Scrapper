# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import  urlopen, Request
from win10toast import ToastNotifier


# %%
header = {"User-Agent" : "Mozzila"}
req = Request("https://www.worldometers.info/coronavirus/country/india", headers= header )
html = urlopen(req)


# %%
html.status


# %%
obj = bs(html)


# %%
new_cases = obj.find("li", {"class": "news_li"}).strong.text.split()[0]


# %%
new_deaths = list(obj.find("li", {"class": "news_li"}).strong.next_siblings)[1].text.split()[0]


# %%
new_deaths


# %%
notifier =  ToastNotifier()


# %%
message = "New Cases: " + new_cases + "\nNumber of Deaths: " + new_deaths


# %%
message


# %%
notifier.show_toast(title = "COVID-19 Daily Updates", msg = message, duration = 5)


# %%



