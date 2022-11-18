# Configuration

debug_mode = True
userinterface_host = '0.0.0.0'
userinterface_port = 80
userinterface_url = f"http://{userinterface_host}:{userinterface_port}/"

userapi_host ='0.0.0.0'
userapi_port = 8000
userapi_url = f"http://{userapi_host}:{userapi_port}/"

modelapi_host = '0.0.0.0'
modelapi_port = 8001
modelapi_url = f"http://{modelapi_host}:{modelapi_port}/"

dataapi_host = '0.0.0.0'
dataapi_port = 8002
dataapi_url = f"http://{dataapi_host}:{dataapi_port}/"

log_level = 'debug'
store_data_url = f"http://{dataapi_host}:{dataapi_port}/store_data"