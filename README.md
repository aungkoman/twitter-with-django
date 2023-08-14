# Twitter with Django


## Bash Logs

ဘယ်ကုတ်တွေ ရေးလဲ?

###  Create Project

```bash
# step 1
# create django project
# mysite is project name 
django-admin startproject twitter

# step 2
# go to django project and run
cd twitter
python manage.py runserver


# step 3
# open http://127.0.0.1:8000/ in browser
# you can see landing page

```

### Create App

```bash
# step 1
# create django app
# tdl is app name
python manage.py startapp users
# step 2
# create urls.py file inside users folder
# type following code in users/urls.py
```

ဒီမှာသာ သွားကြည့်တော့
အလျှင်လိုနေပြီ။


https://github.com/aungkoman/django-hello/blob/main/HOWTO.md


Template (4) ခု လိုမယ်။

- login
- register
- user panel
- update form 

## အရံသင့် လုပ်ပေးထားတာတွေ များလွန်းတယ်။

User Registration နဲ့ တင်တိုင်ပတ်။



- user register အိုကေလား ဆိုတာကို  admin panel မှာ ကြည့်။
login form လုပ်မယ်။



Form ဆောက်ပြီး Manual လုပ်ဖို့ဆိုရင်

https://docs.djangoproject.com/en/4.2/topics/auth/default/

ရိုးရိုး HTML Form ကနေ Data ပို့
view ကနေ လက်ခံပြီး သက်ဆိုင်ရာ Model ဆောက်
Login Method သုံး
Logout သုံး

ဒါဆို Register ရပြီ။

Request မှာလည်း authenticated ဖြစ်နေမယ်။
