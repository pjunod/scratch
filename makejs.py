with open("json.list") as file:
    jlist = file.readlines()

jlist = [x.strip() for x in jlist]
for pattern in jlist:
    payload = dict(attribute={"pattern": pattern, "timestamp": "@timestamp"})
    
    print(payload)
