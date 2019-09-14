from bs4 import BeautifulSoup
import requests
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def get_module_statuses():
    #try:
    module_statuses = []
    entries =  ''
    session = requests.Session()
    retry = Retry(connect = 3, backoff_factor = 0.5)
    adapter = HTTPAdapter(max_retries = retry)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    #Loads link as focus source
    source = session.get('http://emergencywatch.pythonanywhere.com/status/', verify = False).text
    #Creates object with this source
    soup = BeautifulSoup(source, 'lxml').text
    newDictionary = json.loads(str(soup))

    entries = newDictionary['modules']
    for entry in entries:
    # Goes through the soup object and for each class it iterates through some extractions

        module_name = entry['module_name']
        module_status = entry['status']
        last_updated = entry['time']

        module_statuses.append({
            'module_name': module_name,
            'status': module_status,
            'time': last_updated
        })
    print (module_statuses)
    print (entries)
    return entries
    #except Exception:
    #    print ('Error retrieving data... Try again later')
