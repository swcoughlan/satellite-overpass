# satellite-overpass
A script to pull satellite overpass info for a given location from Spectator.Earth and write to a csv. 

Satellites:

Sentinel-1A
Sentinel-1B
Sentinel-2A
Sentinel-2B
Sentinel-3A 
Sentinel-3B
Landsat-8

The data is written to a Google Sheet: https://docs.google.com/spreadsheets/d/1hx5xmfN6G9hyoHuBxPAVrF75SU90OJ8ko_GVUAaGYds/edit#gid=0 
The area of interest can be defined using the variable 'bbox'. It's currently set to Dublin Bay. 

# Steps:

# 1: Set up Google Sheets API
Log in with Techworks Marine Gmail account on GCP console to enable the Google Sheets API: https://support.google.com/googleapi/answer/6158841?hl=en  
Download the API Key in Json format from the account where the code and other packages are located.

# 2: Create a Blank Google Sheet
Create a new Google Sheet with Satellite Overpasses name and copy the Sheet ID from the URL.
Edit the viewing/editing permissions.

# 3: Create a webhook on Teams
A part of code sends the data on Teams group channel as well. Therefore, to send the messages to teams we need to create a webhook in Teams using https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook

# 4: Deploy on AWS Lambda
Download and install the required packages with the overpass script on AWS Lambda and schedule a Cloudwatch event using https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html
