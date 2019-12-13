
import requests

murl = "http://0.0.0.0:5003/ptt"
mdata = {
    "a1": 100
}

resp = requests.get(murl, mdata)

hd = resp.headers

print(resp.text)
print(type(hd))
