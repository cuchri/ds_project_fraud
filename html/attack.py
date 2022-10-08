# Website injection.

import requests

url = 'http://192.168.0.35:8000/form'
data = {
        'signup_time':'07/10/2022 18:49',
		'purchase_value':'10',
		'purchase_time':'08/10/2022 18:49', 
		'device_id':'AANHQRSKUCHIC', 
		'source':'Ads',
		'browser':'FireFox',
		'sex':'M',
        'age':'25',
		'ip_address':'4127598609'
    }
for i in range(1,4) :
    r = requests.post(url, data=data)