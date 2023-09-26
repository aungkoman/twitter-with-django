# Twitter with Django


## 2023-09-26 NewsFeed

NewsFeed လုပ်မယ်။

သတင်းတွေပြမယ်။
Comment ရေးမယ်။

Public မှာ အရင်ပြ။
Comment ရေးချင်ရင် Login ဝင်။



template 
view
url



### Comment ထည့်မယ်။

- [ ] နောက်ပြီး Bootstrap Template တစ်ခု ရှာမယ်။
- [ ] Vuexy ပဲ သုံးမယ်။​လိုတဲ့ Component တွေ အစုံအလင်ပါတယ်။


## Procedure

ဘာလုပ်လုပ် Admin Panel ထဲမှာ အရင်ထည့်မယ်။

Admin Panel မှာ မှန်မှန်ကန်ကန် အလုပ်လုပ်ပြီ။

View နဲ့ Template တွေ ရေးမယ်။

View မှာ Select အရင်လုပ်မယ်။
လောလောဆယ် ဒဲ့ Select တာ မရှိပဲ 

Profile Info မှာ ပြတာပဲ ရှိတယ်။

ဝင်ထားတဲ့ User ရဲ့ Profile Info ကို Pass လုပ်ပေးလိုက်မယ်။


- [x] User Profile Select အဆင်ပြေပြီ။
- [ ] Edit လုပ်မယ်
    - [x] template ထည့်ပြီးပြီ။
    - [x] url နဲ့ view ထည့်မယ်။
    - [x] အိုကေသွားပြီ။​ form field optional တွေ လုပ်ရမယ်။
- [x] Insert လုပ်မယ်။
- [x] Delete လုပ်မယ်။

ဒါဆို Module တစ်ခု ရပြီ။

User Profile Module ရပြီ။

- Post ဆက်လုပ်မယ်။

- Article လုပ်မယ်။

ဘာတွေပါမလဲ?

content
media array 

ဒါပဲ ပါမယ်။
owner ကတော့ User ပေါ့။
ဒါမှ မဟုတ် Profile 

Profile ပဲ ထားမယ်။

Article Model တစ်ခုဆောက်ပြီး Admin Panel မှာ ထည့်ထားပြီးဖြစ်။

- template မှာ လေးခုထည့်မယ်။
    - [x] Article List
    - [x] Article New Form
    - [x] Article Detail
    - [x] Article Edit Form
    - [x] Article Delete ( Data Link )

C နဲ့ R လုပ်တာ မိနစ် (၄၀)​ ကြာ။
U D က မိနစ် (၂၀)။
စုစုပေါင်း (၁)​ နာရီ။

Backbone နဲ့ ရေးခဲ့တဲ့ မိနစ် (၄၀) ကို ရောက်အောင်လုပ်ရမယ်။


ဆက်လုပ်မှာက 

User NewsFeed Page 
Like / Unlike
Comment

ဒီလောက်ဆိုရင် UI ဘက်ကို စလုပ်လို့ရပြီ။



## 2023-09-05 Road Map

- [ ] News Feed Page with pagination
- [ ] Like / Unlike Ajax
- [ ] Article detail with comment selection
- [ ] Create Comment
- [ ] Edit Comment
- [ ] Delete Comment




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


## 2023-08-26 Basic (6) CRUD Modules

- [ ] User
- [ ] Profile
- [ ] Post
- [ ] Like
- [ ] Comment
- [ ] Share


### User

Login Page
Login Business Logic
Register Page
Register Business Logic

- Post Page လုပ်မယ်။

Post ရဲ့ ဖွဲ့စည်းပုံကို အရင်လုပ်ရမယ်။

Post တစ်ခုမှာ
- id
- user
- content
- media [] တွေပါကောင်းပါမယ်။

ဒါပဲ။

ဒါဆို Media ဆိုသည်းသန့်ထားရမလား?


