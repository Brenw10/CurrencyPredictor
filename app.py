import win
import market
import pandas as pd
from datetime import datetime

initials = win.get_complete_initials()
rates = market.get_rates_from_date(initials, 1)
diffs = market.get_diff_from_column("close", rates)

for val in rates:
    print(
        str(pd.to_datetime(val['time'], unit='s')) + " - " + str(val["close"])
    )

# for val in diffs:
#     print(val)
