# Import required packages
import requests
import pandas as pd
from datetime import datetime
from pytz import timezone
import config

# Pull overpass data from Spectator.Earth API
api_key = config.api_key # Insert your api code here
bbox = '-6.15450317,53.30408682,-6.07896861,53.34080955'  # Dublin Bay
satellites = 'Sentinel-1A, Sentinel-1B, Sentinel-2A, Sentinel-2B, Sentinel-3A, Sentinel-3B, Landsat-8'
url = f'https://api.spectator.earth/overpass/?api_key={api_key}&bbox={bbox}&satellites={satellites}'
response = requests.get(url)
data = response.json()

# Extract date and satellite info
overpasses = [{'date': overpass['date'], 'satellite': overpass['satellite']} for overpass in data['overpasses']]
print(overpasses)

# Create a dataframe of results and convert dates
data = pd.DataFrame(overpasses)
data['datetime'] = pd.to_datetime(data['date'])
data['day'] = data['datetime'].dt.day_name()
data['date'] = data['datetime'].dt.date

# Convert datetime to Irish Standard Time (IST) and Coordinated Universal Time (UTC) and add to dataframe
ist_timezone = timezone('Europe/Dublin')
data['ist'] = data['datetime'].apply(lambda x: x.astimezone(ist_timezone).strftime('%H:%M:%S'))
data['utc'] = data['datetime'].dt.strftime('%H:%M:%S')
data.drop(columns=['datetime'], axis=1, inplace=True) # datetime column no longer needed

# Export to CSV
data.to_csv('output/sample.csv', index=False)