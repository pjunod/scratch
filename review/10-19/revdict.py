log_content = """192.168.2.20    [01/01/2020:10:10:10 -0300] "GET /foo/bar"     200     1234          2370
192.168.2.21    [01/01/2020:10:14:31 -0300] "GET /bar"         404     393           32
100.2.238.80    [01/01/2020:10:14:30 -0300] "GET /bar"         404     393           32
192.168.2.20    [01/01/2020:10:11:10 -0300] "GET /foo"         200     6000          1200
192.168.2.20    [01/01/2020:10:12:10 -0300] "GET /foo/bar/baz" 200     9999          1432
100.2.238.80    [01/01/2020:10:12:40 -0300] "GET /foo?q=baz"   400     393           32
100.2.238.80    [01/01/2020:10:13:10 -0300] "GET /foo/bar"     200     1234          300
62.8.38.27      [01/01/2020:10:14:10 -0300] "GET /foo/bar"     200     1234          400
62.8.38.27      [01/01/2020:10:14:20 -0300] "GET /foo/bar"     200     1234          420
62.8.38.27      [01/01/2020:10:14:30 -0300] "GET /foo/bar"     200     1234          423
192.168.2.20    [01/01/2020:10:14:30 -0300] "GET /bar"         404     393           32"""

ip_dict = {}
for i in log_content.split('\n'):
    ip = i.split()[0]
    if ip in ip_dict:
        ip_dict[ip] += 1
    else:
        ip_dict[ip] = 1

print(ip_dict)
print("")

ip_sorted = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(ip_sorted)

print(sorted_dict)
print("")

ip_list = list(sorted_dict.keys())
for k in ip_list[:3]:
    print(f"{k}:\t{sorted_dict[k]}")