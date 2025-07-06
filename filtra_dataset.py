import pandas as pd
from glob import glob

stations = pd.read_csv('dataset/stations.csv')
stations.record_first = pd.to_datetime(stations.record_first)
stations.record_last = pd.to_datetime(stations.record_last)
stations["period_size"] = stations.record_last - stations.record_first
stations.period_size = stations.period_size.dt.days

filelist = glob('dataset_raw/weather_*.csv')

idx = stations.groupby('region')['period_size'].idxmax()
stations_longest = stations.loc[idx].sort_values('region')
for filename in filelist:
    data = pd.read_csv(filename)
    data = data[data.ESTACAO.isin(stations_longest.id_station)]
    data.to_csv(filename.replace('.csv', '_filtered.csv'), index=False)
