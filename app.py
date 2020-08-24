import win
import market
import pandas as pd
from datetime import datetime

start_date = win.get_start_date_period()
initials = win.get_complete_initials()

rates = market.get_rates_from_date(initials, start_date)
diffs = market.get_diff_from_column("close", rates)

for val in rates:
    print(
        str(pd.to_datetime(val['time'], unit='s')) + " - " + str(val["close"])
    )


for val in diffs:
    print(val)

print(str(pd.to_datetime(rates[0]['time'], unit='s')
          ) + " - " + str(rates[0]["close"]))
print(start_date)
print(len(rates))
print(len(diffs))
