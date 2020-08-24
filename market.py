from datetime import datetime, timedelta
import MetaTrader5 as mt5


def get_rates_from_date(initials, days_decrease, show_last=False):
    mt5.initialize()

    values = mt5.copy_rates_range(
        initials,
        mt5.TIMEFRAME_M1,
        datetime(2020, 8, datetime.now().day) - timedelta(days=days_decrease),
        datetime(2020, 8, datetime.now().day + 1)
    )

    mt5.shutdown()

    return values if show_last else values[:-1]


def get_diff_from_column(column, rates):
    diff = []
    for i in range(1, len(rates)):
        diff.append(rates[i][column] - rates[i-1][column])
    return diff
