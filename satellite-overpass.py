# import required packages
import requests
import pandas as pd
import config

# pull overpass data from Spectator.Earth API
api_key = config.api_key 
bbox = '-6.15450317,53.30408682,-6.07896861,53.34080955' # Dublin Bay
satellites = 'Sentinel-1A, Sentinel-1B, Sentinel-2A, Sentinel-2B, Sentinel-3A, Sentinel-3B,Landsat-8'
url = 'https://api.spectator.earth/overpass/?api_key={api_key}&bbox={bbox}&satellites={satellites}'.format(api_key=api_key, bbox=bbox, satellites=satellites)
response = requests.get(url)
data = response.json()

# loop through results to extract date and satellite info
result = []
for i in range(len(data['overpasses'])):
  overpass = {}
  overpass['date'] = data['overpasses'][i]['date']
  overpass['satellite'] = data['overpasses'][i]['satellite']
  result.append(overpass)

# create dataframe of results & convert datetime to day, date, Irish Standard Time, Coordinated Universal Time
data = pd.DataFrame(result, columns=['satellite', 'date'])
data['Day'] = pd.to_datetime(data['date']).dt.day_name()
data['Date'] = pd.to_datetime(data['date']).dt.date
data['IST'] = pd.DatetimeIndex(pd.to_datetime(data['date'])).tz_convert('Europe/Dublin')
data['IST'] = pd.to_datetime(data['IST']).dt.strftime('%H:%M:%S')
data['UTC'] = pd.to_datetime(data['date']).dt.strftime('%H:%M:%S')
data.pop('date') 
data = data.rename(columns={'satellite': 'Satellite'})

# export to csv
data.to_csv('output/sample.csv', index=False)