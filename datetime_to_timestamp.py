#Author: Hossein Zolfaghari
#Company: PROMES-CNRS, SESA
#July 2022

import datetime


#datetime should be in this format '2022-06-15 11:44:30' otherwise the code should be changed 
#Output is timestamp
def datetime_to_timestamp(datetime):
    Yc = int(datetime[-19:-15])
    mc = int(datetime[-14:-12])
    dc = int(datetime[-11:-10])
    Hc = int(datetime[-8:-6])
    Mc = int(datetime[-5:-3])
    Sc = int(datetime[-2:])
    DateTimeImage = datetime.datetime(Yc, mc, dc, Hc, Mc, Sc).isoformat(' ')
    # DateTimeImages_last_UTC.append(DateTimeImage)
    DateTimeImage = pd.to_datetime(DateTimeImage,infer_datetime_format = True)
    your_timestamp = int(round(DateTimeImage.timestamp()))
    return your_timestamp
