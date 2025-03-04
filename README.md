# PASFI
Filter password lists based on password policies

# Usage

Start by checking the app's password policy. You can do it by trying to register a new account and entering a very weak password (i.e: `1234`) which you know it will be rejected. 

This rejection usually comes with more details, such as: `Minimum 10 characters, with 1 capital letter and 1 digit`

And here's your starting point!

People are lazy when it comes to picking a password. They will do the minimum necessary to pass the limitation and get their password approved.

# Example - offsec

Now that we know the minimum password requirements, we can use `pasfi.py` + a common password list (i.e: `rockyou.txt`) to extract only the passwords that match your criteria.

For example, the command below will extract all passwords of 8 characters that contain 1 capital letter, 1 digit and 1 special character from rockyou.txt

C:\users> python3 pasfi.py rockyou.txt --length 8 --caps 1 --digits 1 --specials 1

```
P@ssw0rd
Hottie#1
Ashley#1
v,iiy9oN
Zaq1@wsx
Chivas#1
ryoT,b9i
Mortty*8
Marine#1
```

# Example - blueteam

As a system administrator or product owner, you want to make sure your app enforces a strong password policy.

However, many of the passwords present in data leaks may follow your policies - but this doesn't make them safe to use.

Use your password policiy in combination with publicly available lists of password leaks to create a blacklist of passwords.

This way you enforce not only a strong password policy, but you prevent your users from using a common password that is present in hacker's lists.
