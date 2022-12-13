import base64
import requests 
from requests.auth import HTTPBasicAuth


url = "https://api.plataforma.ipn.mx/publico/general/secure/renapo/curp/consultar"
user = "deyssuser"
password = "p5HHNbdq7JUt5Hnqwv2erWva6hPbKtk8"
curp = "GOCM971029HDFNRG03"



json = "{" + "\"data\":{" + "\"curp\":" + "\"" + curp + "\"" + "} }"
request = requests.post(url, auth = HTTPBasicAuth(user,password), data=json)
if(request != None):
    try:
        jsonData=request.json()
        #print(jsonData)
        if(jsonData.get('@statusOper') == "EXITOSO"):
            print(jsonData)
        elif(jsonData.get('@statusOper') == "NO EXITOSO"):
            print(jsonData)
    except:
        print("No se pudo realizar la solicitud")
else:
    print("No se pudo realizar la solicitud")