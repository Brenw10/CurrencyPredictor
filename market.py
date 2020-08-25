from datetime import datetime, timedelta
import MetaTrader5 as mt5


def get_rates_from_start_date(initials, start_date, show_last=False):
    mt5.initialize()

    values = mt5.copy_rates_range(
        initials,
        mt5.TIMEFRAME_M1,
        start_date,
        datetime(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day + 1
        )
    )

    mt5.shutdown()

    return values if show_last else values[:-1]
