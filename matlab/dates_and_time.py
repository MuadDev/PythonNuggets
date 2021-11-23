# %%
# How to convert a Matlab datenum to a Python datetime?
from datetime import datetime, timedelta

def datenum_to_datetime(dn: float) -> datetime:
    """Converts a Matlab datenum to a Python datetime
    
    From: https://stackoverflow.com/a/13965852/8488985

    Example:
        >>> dn = 731965.04835648148
        >>> datenum_to_datetime(dn)
        datetime.datetime(2004, 1, 19, 1, 9, 38)
    """
    return datetime.fromordinal(int(dn)) + timedelta(days=dn % 1) - timedelta(days = 366)

# %%
# How to convert Python datetime a to a Matlab datenum?
from datetime import datetime, timedelta


def datetime_to_datenum(dt: datetime) -> float:
    """Converts a Python datetime to a Matlab datenum

    From: https://stackoverflow.com/a/9391765/8488985

    Example:
        >>> dt = datetime(2004, 1, 19, 1, 9, 38)
        >>> datetime_to_datenum(dt)
        731965.04835648148
    """
    mdn = dt + timedelta(days=366)
    frac_seconds = (dt - datetime(dt.year, dt.month, dt.day, 0, 0, 0)).seconds / (24.0 * 60.0 * 60.0)
    frac_microseconds = dt.microsecond / (24.0 * 60.0 * 60.0 * 1000000.0)
    return mdn.toordinal() + frac_seconds + frac_microseconds

if __name__ == "__main__":
    import doctest
    doctest.testmod()