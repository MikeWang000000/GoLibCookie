import http.cookies
import requests
import json
import time

cookie_string = "Authorization=eyJOR3xyEPGYYg88SBKwLLVF4YbspERVXSLK.eyJ17WDNVh83TpBnrEBpuGRNFtDVKpnWynUTmVRaL22Q7MsUZgPgT7hmDvxm68bf6pMD3g.dgLLR6EhU-3gtVFSwhcenRqZMPd7yzq2bULMApKeGN8KbweFE2jHJHes4PDwxxwNwSKdDtF3EG8VnrPqTFaudVbydcUGgQbaVxRSgbBVCsC6eRL7-entRnGyr5Q3bEcWKaBJM8DMwPh3RtR7DnwtdXFg2mLdUMthhDynj9R-bNErdzQt7zK8k9F9HPfVxzdaVcmBUgwcp2YqUP-wNVhfwBJu2XpvawJPNNEhEHeBP7ysU7BTXNLvyn5H3-Lns93S7kapG-Ugn8wkk3Hg8svAbfwTu2W7RbxVr_Yud_9EBJ5h7TVG2PebYdqf7C_vK2wKJLkMqegy94dyhP6ba_6vdx; SERVERID=545b6d8d091f13d9ce1bf0321587bf07|1633082400|1633082400; SERVERID=f7dde79ccada9f4171454d57b0848c4a|1633082400|1633082400"

session = requests.Session()
cookie = http.cookies.SimpleCookie()
cookie.load(cookie_string)
for key, morsel in cookie.items():
    session.cookies.set(key, morsel)

while True:
    if session.cookies.keys().count("Authorization") > 1:
        session.cookies.set("Authorization", domain="", value=None)
    res = session.post("http://wechat.v2.traceint.com/index.php/graphql/", json={
        "query": 'query getUserCancleConfig { userAuth { user { holdValidate: getSchConfig(fields: "hold_validate", extra: true) } } }',
        "variables": {},
        "operationName": "getUserCancleConfig"
    })
    try:
        result = res.json()
    except json.decoder.JSONDecodeError as err:
        print("Error: %s" % err)
        break
    if result.get("errors") and result.get("errors")[0].get("code") != 0:
        print("Session expired!")
        break
    print("Session OK.")
    time.sleep(60)
