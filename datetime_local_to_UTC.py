import pandas as pd
from dateutil import tz

def datetime_local_to_UTC(local_datetime):
        DateTimeImage = pd.to_datetime(local_datetime,infer_datetime_format = True)
        datetime_utc=DateTimeImage.replace(tzinfo=tz.tzlocal()).astimezone('UTC')
        return datetime_utc