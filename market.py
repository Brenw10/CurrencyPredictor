import MetaTrader5 as mt5


def get_rates_from_date(initials, start_date, end_date, show_last=False):
    mt5.initialize()

    values = mt5.copy_rates_range(
        initials,
        mt5.TIMEFRAME_M5,
        start_date,
        end_date
    )

    mt5.shutdown()

    return values if show_last else values[:-1]
