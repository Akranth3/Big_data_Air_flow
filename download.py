import pycurl
import certifi
import yaml

c = pycurl.Curl()
base_url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/'

# Load parameters from params.yaml
with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f)

year = params['year'] + '/'
file_name = params['file_location']
print(year, file_name)


url = base_url + year + file_name

c.setopt(c.URL, url)
c.setopt(c.CAINFO, certifi.where())
with open('Data/data.csv', 'wb') as f:
    c.setopt(c.WRITEDATA, f)
    c.perform()
c.close()

