# Configuration
"""
userinterface, userapi, modelapi, dataapi, store data csv, log level for fastapi
"""
debug_mode = True
userinterface_host = '172.30.0.10'
userinterface_port = 80
userinterface_url = f"http://{userinterface_host}:{userinterface_port}/"

userapi_host ='172.30.0.11'
userapi_port = 8000
userapi_url = f"http://{userapi_host}:{userapi_port}/"

modelapi_host = '172.30.0.12'
modelapi_port = 8001
modelapi_url = f"http://{modelapi_host}:{modelapi_port}/"

dataapi_host = '172.30.0.13'
dataapi_port = 8002
dataapi_url = f"http://{dataapi_host}:{dataapi_port}/"

store_data_url = f"http://{dataapi_host}:{dataapi_port}/store_data"

log_level = 'debug'