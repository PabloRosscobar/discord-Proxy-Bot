token = "BOT TOKEN"
# Your token is required for this bot to work.

import discord
import logging
import time
from collections import Counter
import asyncio
import json
import datetime
import requests
import qrcode
from discord import Embed
import firebase
from random import randint
import random
import re
import string
import pyrebase
import base64
from discord_webhook import DiscordEmbed, DiscordWebhook


session = requests.session()

client = discord.Client()
# Defines the discord client.

name = "Resi Bot"
prefix = "!"
# Some definitions for this bots own usage.

logging.basicConfig(level=logging.INFO)
# Sets the logging level.

username = ''
password = ''

@client.event
async def on_ready():
    activity = discord.Game(name="Pro Resi Bot")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("-------------")
    print(name + ". Running as " + client.user.name)
    print("-------------")
# Shows message on boot and sets game.

async def createProxy(username,password,proxy_authkey,country,PAmount,Ptype,planType):
    # This is where we gen the proies themselves
    # first selects correct plan depending on user purchase
    if 'BP' in planType:
        username = username.lower()
        letters = string.ascii_lowercase
        proxies = []
        # chooses correct code for static or rotating proxies
        if Ptype.lower() == 'static':
            for i in range(0,int(PAmount)): 
                # generates random session values for number needed     
                randsess = ''.join(random.choice(letters) for i in range(8))
                randsess = f"{randsess}{str(randint(10,99))}" 
                gen = f"YOUR.DOMAIN.HERE:31112:{username}:{proxy_authkey}_country-{country}_session-{randsess}"
                
                proxies.append(gen)
            # returns list of proxies to main gen file 
            return proxies
        else:

            for i in range(0,int(PAmount)): 
                gen = f"YOUR.DOMAIN.HERE:31112:{username}:{proxy_authkey}_country-{country}"
                proxies.append(gen)

            return proxies

    else:
        letters = string.ascii_lowercase
        proxies = []
        # chooses correct code for static or rotating proxies
        if Ptype.lower() == 'static':

            for i in range(0,int(PAmount)):
              
                if country == 'EU':
                    euCountries = ["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","GB","HU","IE","IT","LV","LT","LU","MT","NL","PO","PT","RO","SK","SI","ES","SE"]
                    countryToUse = random.choice(euCountries)
                    randsess = ''.join(random.choice(letters) for i in range(5))
                    randsess = f"COMPANYNAME{randsess}{str(randint(10,99))}" 
                    gen = f"pro.DOMAIN.HERE:10002:user-{username}-country-{countryToUse}-session-{randsess}:{password}"
                    proxies.append(gen)

                elif 'MESH' in country:
                    randsess = ''.join(random.choice(letters) for i in range(5))
                    randsess = f"COMPANYNAME{randsess}{str(randint(10,99))}" 
                    gen = f"mesh.DOMAIN.HERE:10002:user-{username}-session-{randsess}:{password}"
                    proxies.append(gen)
                
                elif 'COURIR' in country:
                    euCountries = ["FR","DE","GB","IT"]
                    countryToUse = random.choice(euCountries)
                    randsess = ''.join(random.choice(letters) for i in range(5))
                    randsess = f"COMPANYNAME{randsess}{str(randint(10,99))}" 
                    gen = f"pro.DOMAIN.HERE:10222:user-{username}-country-{countryToUse}-session-{randsess}:{password}"
                    proxies.append(gen)

                else:
                    countryToUse = country
                    pass
                    # generates random session values for number needed 
                    randsess = ''.join(random.choice(letters) for i in range(5))
                    randsess = f"COMPANYNAME{randsess}{str(randint(10,99))}" 
                    gen = f"pro.DOMAIN.HERE:10002:user-{username}-country-{countryToUse}-session-{randsess}:{password}"
                    proxies.append(gen)

            return proxies
        else:

            for i in range(0,int(PAmount)): 
                if country == 'EU':
                    euCountries = ["AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","GR","GB","HU","IE","IT","LV","LT","LU","MT","NL","PO","PT","RO","SK","SI","ES","SE"]
                    countryToUse = random.choice(euCountries)
                    gen = f"pro.DOMAIN.HERE:10002:user-{username}-country-{countryToUse}:{password}"
                    proxies.append(gen)

                elif 'MESH' in country: 
                    gen = f"mesh.DOMAIN.HERE:10002:user-{username}:{password}"
                    proxies.append(gen)
                elif 'COURIR' in country:
                    euCountries = ["FR","DE","GB","IT"]
                    countryToUse = random.choice(euCountries)
                    gen = f"pro.DOMAIN.HERE:10222:user-{username}-country-{countryToUse}:{password}"
                    proxies.append(gen)

                else:
                    countryToUse = country
                    gen = f"pro.DOMAIN.HERE:10002:user-{username}-country-{countryToUse}:{password}"
                    proxies.append(gen)
           
            return proxies

async def embedErrorGen(error):

    errorEmbed = Embed(
        title=f"CompanyName",
        colour=0x9400D3,
        url="https://DOMAIN.HERE",
    )
    errorEmbed.add_field(
        name="ERROR",
        value=error,
        inline=False
        )

    errorEmbed.set_footer(
        text="CompanyName. All rights reserved.",
        icon_url="COMPANY LOGO LINK"
    )

    return errorEmbed

async def checkRegion(region):
   
    # takes region entered and turns into correct valu for proxy format

    if 'MESH' in region:
        return region
    elif 'COURIR' in region:
        return region
    elif 'UK' in region:
        region = 'GB'
        return region
    else:
        countries = ["US","CA","EU","GB","DE","FR","ES","IT","SE","GR","PT","NL","BE","RU","UA","PL","IL","TR","AU","MY","TH","KR","JP","PH","SG","CN","HK","TW","IN","PK","IR","ID","AZ","KZ","AE","MX","BR","AR","CL","PE","EC","CO","ZA","EG","AO","CM","CF","TD","BJ","ET","DJ","GM","GH","KE","LR","MG","ML","MR","MU","MA","MZ","NG","SN","SC","ZW","SS","SD","TG","TN","UG","ZM","AF","BH","BD","BT","MM","KH","IQ","JO","LB","MV","MN","OM","QA","SA","TM","UZ","YE","AL","AD","AT","AM","BA","BG","BY","HR","CY","CZ","DK","EE","FI","GE","HU","IS","IE","LV","LI","LT","LU","MC","MD","ME","NO","RO","RS","SK","SI","CH","MK","BS","BZ","VG","CR","CU","DM","HT","HN","JM","AW","PA","PR","TT","FJ","NZ","BO","PY","UY","CI","SY"]

        if region in countries:
            return region
        else:
            return False


async def polarGen(message):

    try:
        channel = message.channel
        # Start of proxy authentication + generation, first checks if users exists (set in login function)
        user = message.author.id
        
        config = {
            "apiKey": "API KEY",
            "authDomain": ".firebaseapp.com",
            "databaseURL": "YOUR DATABASE URL",
            "storageBucket": ".appspot.com",
            "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
            }

        firebase = pyrebase.initialize_app(config)
        orders = []
        logins = []
        db = firebase.database()
        inventory = db.child('orders').get()
        Userlogins = db.child('Active Logins').get()
        # gets json data of all orders (this might need changed in fture if we have too many orders)
        for order in inventory.each():
            orders.append(order.val())
        for logg in Userlogins.each():
            logins.append(logg.val())
    except Exception as e:
        print(e)
        return on_ready()

    try:

        for login in logins:
            if str(user) in str(login['Discord ID']):
                orderNumb = login['Order ID']

        for orderr in orders:
            if str(orderNumb) in str(orderr["PlanDetails"]["Order ID"]):
                if orderr['Status'] == 'Active':
                    username = orderr["PlanDetails"]['loginUsername']
                    password = orderr["PlanDetails"]['loginPassword']
                    proxy_authkey = orderr["PlanDetails"]["proxy_authkey"]
                    planType = orderr["PlanDetails"]["type"]
                    try:    
                        mess = message.content
 
                        region = mess.split(' ')[1].upper()
                        Ptype = mess.split(' ')[2].lower()
                        PAmount = 25
                  
                    except:
                        errorEmbed = await embedErrorGen("Error reading quick gen message")
                        await channel.send(embed= errorEmbed)
                        await on_ready()
                        
                    try:

                        checky = await checkRegion(region)
                        if checky == False:
                            errorEmbed = await embedErrorGen("Error reading region, please check and try again")
                            await channel.send(embed= errorEmbed)
                            await on_ready()
                        else:
                            country = region
                            pass

                    except:
                        errorEmbed = await embedErrorGen("Error reading quick gen message")
                        await channel.send(embed= errorEmbed)
                        await on_ready()
                        
                    try:
                        if "PP" in planType:
                            proxies = await createProxy(username,password,proxy_authkey,country,PAmount,Ptype,planType)
                        else:
                            errorEmbed = await embedErrorGen("Error QR gen is only available on Pro plans")
                            await channel.send(embed= errorEmbed)
                            await on_ready()


                        open(f"{username}.txt", 'w').close()
                        for i in proxies:
                            with open(f"{username}.txt", "a") as file:
                                file.write(i+'\n')

                        with open(f"{username}.txt", 'r') as f:
                            proxylist = f.read()


                            f.close()


                    
                        open(f"{username}QR.png", 'w').close()
                        
                        qr = qrcode.QRCode(
                                version=1,
                                box_size=10,
                                border=5)
                        qr.add_data(proxylist)
                        qr.make(fit=True)
               
                        img = qr.make_image(fill='black', back_color='white')

                        img.save(f"{username}QR.png")
               

                        with open(f"{username}QR.png", 'rb') as f:
                            picture = discord.File(fp=f,filename=f"{username}QR.png")
                            helpEmbed = Embed(
                                title=f"CompanyName",
                                colour=0x9400D3,
                                url="https://DOMAIN.HERE",
                            )
                            helpEmbed.set_image(
                                url= f"attachment://{username}QR.png"
                                )
                            helpEmbed.set_footer(
                                text="CompanyName. All rights reserved.",
                                icon_url="COMPANY LOGO LINK"
                            )
                            
                            await channel.send(file=picture,embed=helpEmbed)
                    except Exception as e:
                        print(e)
                        await on_ready()
    except Exception as e:
        print(e)
        await on_ready()


@client.event
async def genProxies(message):
    if isinstance(message.channel, discord.channel.DMChannel):
        try:
            channel = message.channel
            # Start of proxy authentication + generation, first checks if users exists (set in login function)
            user = message.author.id
            
            config = {
                "apiKey": "API KEY",
                "authDomain": ".firebaseapp.com",
                "databaseURL": "YOUR DATABASE URL",
                "storageBucket": ".appspot.com",
                "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
                }

            firebase = pyrebase.initialize_app(config)
            orders = []
            logins = []
            db = firebase.database()
            inventory = db.child('orders').get()
            Userlogins = db.child('Active Logins').get()
            # gets json data of all orders (this might need changed in fture if we have too many orders)
            for order in inventory.each():
                orders.append(order.val())
            for logg in Userlogins.each():
                logins.append(logg.val())
        except Exception as e:
            print(e)
            return on_ready()

        try:

            for login in logins:
                if str(user) in str(login['Discord ID']):
                    orderNumb = login['Order ID']

            for orderr in orders:

                if str(orderNumb) in str(orderr["PlanDetails"]["Order ID"]):
                    if orderr['Status'] == 'Active':
                        username = orderr["PlanDetails"]['loginUsername']
                        password = orderr["PlanDetails"]['loginPassword']
                        proxy_authkey = orderr["PlanDetails"]["proxy_authkey"]
                        planType = orderr["PlanDetails"]["type"]
                        try:
                            

                            timeEmbed = Embed(
                                title=f"CompanyName",
                                colour=0x9400D3,
                                url="https://DOMAIN.HERE",
                            )
                            timeEmbed.add_field(
                                name="TIMEOUT",
                                value="Your session has run out, please start a new session",
                                inline=False
                                )

                            timeEmbed.set_footer(
                                text="CompanyName. All rights reserved.",
                                icon_url="COMPANY LOGO LINK"
                            )


                            embed = Embed(
                                title=f"CompanyName",
                                colour=0x9400D3,
                                url="https://DOMAIN.HERE",
                            )
                            embed.add_field(
                                name="REGION",
                                value="What region would you like to generate? (ISO code)",
                                inline=False
                                )

                            embed.set_footer(
                                text="CompanyName. All rights reserved.",
                                icon_url="COMPANY LOGO LINK"
                            )
                            messageKey = await channel.send(embed= embed)
                            

                            
                            await asyncio.sleep(0.5)
                    
                            try:
                                region = await client.wait_for('message', timeout=60.0)
                                region = region.content.upper()
                            except asyncio.TimeoutError:
                                await channel.send(embed=timeEmbed)
                                await on_ready()

                            await asyncio.sleep(0.5)
                            

                            checky = await checkRegion(region)

                            if checky == False:
                                errorEmbed = await embedErrorGen("Error reading region, please check and try again")
                                await channel.send(embed= errorEmbed)
                                await on_ready()
                            else:
                                country = checky
                            
                        except Exception as e:
                            errorEmbed = await embedErrorGen("Error reading region, please check and try again")
                            await channel.send(embed= errorEmbed)
                            await on_ready()


                        embed = Embed(
                            title=f"CompanyName",
                            colour=0x9400D3,
                            url="https://DOMAIN.HERE",
                        )
                        embed.add_field(
                            name="TYPE",
                            value="What type would you like to generate? (static or rotating)",
                            inline=False
                            )

                        embed.set_footer(
                            text="CompanyName. All rights reserved.",
                            icon_url="COMPANY LOGO LINK"
                        )

                        
                        try:
                            await messageKey.edit(embed=embed)
                        except:
                            await on_ready()
                        
                        try:
                           
                            await asyncio.sleep(0.5)

                            def checkType(user):
                                return user != messageKey.author.id 

                            Ptype = await client.wait_for('message', timeout=60.0, check=checkType)
                
                            
                            try:
                                Ptype = Ptype.content
                            except:
                                errorEmbed = await embedErrorGen("Error reading proxy type, please check and try again")
                                await channel.send(embed= errorEmbed)
                                await on_ready()

                        except Exception as e:
                            errorEmbed = await embedErrorGen("Error reading proxy type, please check and try again")
                            await channel.send(embed= errorEmbed)
                            await on_ready()

                        embed = Embed(
                            title=f"CompanyName",
                            colour=0x9400D3,
                            url="https://DOMAIN.HERE",
                        )
                        embed.add_field(
                            name="AMOUNT",
                            value="How many proxies would you like to generate? (max 1000)",
                            inline=False
                            )

                        embed.set_footer(
                            text="CompanyName. All rights reserved.",
                            icon_url="COMPANY LOGO LINK"
                        )

                        try:
                            await messageKey.edit(embed=embed)
                        except:
                            await on_ready()

                        try:
                            await asyncio.sleep(0.5)

                            def checkNumb(user):
                                return user != messageKey.author.id

                            PAmount = await client.wait_for('message', timeout=60.0, check=checkNumb) 
                            
                            try:
                                PAmount = PAmount.content
                            except:

                                errorEmbed = await embedErrorGen("Error reading amount of proxies, please check and try again")
                                await channel.send(embed= errorEmbed)
                                await on_ready()

                                
                            
                        except Exception as e:
                            errorEmbed = await embedErrorGen("Error reading amount of proxies, please check and try again")
                            await channel.send(embed= errorEmbed)
                            await on_ready()
                            

                        try:
                            await messageKey.delete()
                        
                        except:
                            pass



                        if 'failed' in country:
                            await channel.send(f'Region not found, please try again...')
                        else:

                            try:
                                proxies = await createProxy(username,password,proxy_authkey,country,PAmount,Ptype,planType)
                                
                                fileEmbed = Embed(
                                    title=f"CompanyName",
                                    colour=0x9400D3,
                                    url="https://DOMAIN.HERE",
                                )
                                fileEmbed.add_field(
                                    name="SUCCESS",
                                    value="Proxies successfully generated, please refer to the attached file.",
                                    inline=False
                                    )

                                fileEmbed.set_footer(
                                    text="CompanyName. All rights reserved.",
                                    icon_url="COMPANY LOGO LINK"
                                )
                                await channel.send(embed= fileEmbed)

                                # writes proxies to file
                                open(f"{username}.txt", 'w').close()
                                for i in proxies:
                                    with open(f"{username}.txt", "a") as file:
                                        file.write(i+'\n')
                                
                                # send file to Discord in message
                                with open(f"{username}.txt", "rb") as file:
                                    await channel.send("", file=discord.File(file, f"{username}.txt"))
                            except Exception as e:
                                errorEmbed = await embedErrorGen("Error sending proxy file, please try again later")
                                await channel.send(embed= errorEmbed)
                                
                                print(e)
                                await on_ready()
        except Exception as e:
            errorEmbed = await embedErrorGen("Error getting proxy plan details")
            await channel.send(embed= errorEmbed)
            
            print(e)
            await on_ready()



@client.event
async def fetchData(message):
    # makes sure user exists (set in login function)
    try:
        
        channel = message.channel
        # Start of proxy authentication + generation, first checks if users exists (set in login function)
        user = message.author.id
        
        
        config = {
            "apiKey": "API KEY",
            "authDomain": ".firebaseapp.com",
            "databaseURL": "YOUR DATABASE URL",
            "storageBucket": ".appspot.com",
            "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
            }

        firebase = pyrebase.initialize_app(config)
        orders = []
        logins = []
        db = firebase.database()
        inventory = db.child('orders').get()
        Userlogins = db.child('Active Logins').get()
        # gets json data of all orders (this might need changed in fture if we have too many orders)
        for logg in Userlogins.each():
            logins.append(logg.val())
        for order in inventory.each():
            orders.append(order.val())

        for login in logins:
            if str(user) in str(login['Discord ID']):
                orderNumb = login['Order ID']
        for orderr in orders:
            if str(orderNumb) in str(orderr["PlanDetails"]["Order ID"]):
                if orderr['Status'] == 'Active':
                    proxyDeets = orderr['PlanDetails']
                    userD = str(message.author.id)
                    Pplan = proxyDeets['type']
                    userID = proxyDeets['loginUsername']
                    pAuth = proxyDeets['proxy_authkey']
                    orderID = proxyDeets['Order ID']
                    # variables are set and discord user ID is validated 
                    if userD in proxyDeets['Discord ID']:
                        totalDataLeft, dayUsage, weekUsage, monthUsage, totalUsed = await getdataLeft(Pplan,userID,message)
                        # id discord user is corrrect, retuns data left on plan

                        if totalDataLeft <= 0:
                            Pdetails = {
                            'Available': 0
                            }
                            db.child('orders').child(orderID).child('Available').update(Pdetails)

                            Pdetails = {
                            'Status': 'Closed'
                            }
                            db.child('orders').child(orderID).update(Pdetails)

                        dataEmbed = Embed(
                            title=f"CompanyName",
                            colour=0x9400D3,
                            url="https://DOMAIN.HERE",
                        )
                        dataEmbed.add_field(
                            name="DATA USAGE",
                            value=f"Information about your PRO PLAN:",
                            inline=False
                            )
                        dataEmbed.add_field(
                            name="DATA LEFT",
                            value=f"{str(totalDataLeft)}GB",
                            inline=False
                            )
                        dataEmbed.add_field(
                            name="DATA USED",
                            value=f"{str(totalUsed)}GB",
                            inline=False
                            )
                        dataEmbed.add_field(
                            name="DATA USED - LAST 24 HOURS",
                            value=f"{str(dayUsage)}GB",
                            inline=False
                            )
                        dataEmbed.add_field(
                            name="DATA USED - LAST 7 DAYS",
                            value=f"{str(weekUsage)}GB",
                            inline=False
                            )
                        dataEmbed.add_field(
                            name="DATA USED - LAST MONTH",
                            value=f"{str(monthUsage)}GB",
                            inline=False
                            )

                        dataEmbed.set_footer(
                            text="CompanyName. All rights reserved.",
                            icon_url="COMPANY LOGO LINK"
                        )

                        if isinstance(message.channel, discord.channel.DMChannel):
                            await channel.send(embed= dataEmbed)
                        else:
                            errorEmbed = await embedErrorGen('Please only send comamands in DM')
                            await channel.send(embed= errorEmbed)
                            await on_ready()

                        break
                    else:
                        errorEmbed = await embedErrorGen('Username does not match, please login and try again')
                        await channel.send(embed= errorEmbed)
                        await on_ready()
                     
    except Exception as e:
        print(e)
        await on_ready()



async def fastGen(message):

    if isinstance(message.channel, discord.channel.DMChannel):
        try:
            channel = message.channel
            # Start of proxy authentication + generation, first checks if users exists (set in login function)
            user = message.author.id
            
            config = {
                "apiKey": "API KEY",
                "authDomain": ".firebaseapp.com",
                "databaseURL": "YOUR DATABASE URL",
                "storageBucket": ".appspot.com",
                "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
                }

            firebase = pyrebase.initialize_app(config)
            orders = []
            logins = []
            db = firebase.database()
            inventory = db.child('orders').get()
            Userlogins = db.child('Active Logins').get()
            # gets json data of all orders (this might need changed in fture if we have too many orders)
            for order in inventory.each():
                orders.append(order.val())
            for logg in Userlogins.each():
                logins.append(logg.val())
        except Exception as e:
            print(e)
            return on_ready()

        try:

            for login in logins:
                if str(user) in str(login['Discord ID']):
                    orderNumb = login['Order ID']

            for orderr in orders:
                if str(orderNumb) in str(orderr["PlanDetails"]["Order ID"]):
                    if orderr['Status'] == 'Active':
                        username = orderr["PlanDetails"]['loginUsername']
                        password = orderr["PlanDetails"]['loginPassword']
                        proxy_authkey = orderr["PlanDetails"]["proxy_authkey"]
                        planType = orderr["PlanDetails"]["type"]
                        try:    
                            mess = message.content
    
                            region = mess.split(' ')[1].upper()
                            Ptype = mess.split(' ')[2].lower()
                            PAmount = mess.split(' ')[3]
                    
                        except:
                            errorEmbed = await embedErrorGen("Error reading quick gen message")
                            await channel.send(embed= errorEmbed)
                            await on_ready()
                            
                        try:
                            checky = await checkRegion(region)
                            if checky == False:
                                errorEmbed = await embedErrorGen("Error reading region, please check and try again")
                                await channel.send(embed= errorEmbed)
                                await on_ready()
                            else:
                                country = region
                                pass

                        except:
                            errorEmbed = await embedErrorGen("Error reading quick gen message")
                            await channel.send(embed= errorEmbed)
                            await on_ready()
                            
                        try:
                            proxies = await createProxy(username,password,proxy_authkey,country,PAmount,Ptype,planType)
                    
                            # writes proxies to file
                            open(f"{username}.txt", 'w').close()
                            for i in proxies:
                                with open(f"{username}.txt", "a") as file:
                                    file.write(i+'\n')
                            
                            # send file to Discord in message
                            with open(f"{username}.txt", "rb") as file:
                                await channel.send("Your proxies:", file=discord.File(file, f"{username}.txt"))
                        except Exception as e:
                            print(e)
                            return on_ready()
        except Exception as e:
            print(e)
            return on_ready()


async def helpMessage(message):
    

    channel = message.channel

    helpEmbed = Embed(
        title=f"CompanyName",
        colour=0x9400D3,
        url="https://DOMAIN.HERE",
    )
    helpEmbed.add_field(
        name="**__HOW TO LOGIN__**",
        value="To login to your proxy plan, DM '!login username pasword' to the ProResiBot depending on which plan you have purchased.\n\nFor example:\n*!login BMPWPioI000 uj8yhst7R*\n",
        inline=False
        )
    helpEmbed.add_field(
        name="**__HOW TO GEN PROXIES__**",
        value="To generate proxies, DM '!gen' to the ProResiBot depending on which plan you have purchased.\nThe bot will then respond with instructions on how to proceed from there.",
        inline=False
        )
    helpEmbed.add_field(
        name="**__HOW TO USE FAST GEN__**",
        value="To use fast gen mode, DM '!fast' followed by the region, type and amount you want ProResiBot.\n\nFor example:\n*!fast FR static 500*",
        inline=False
        )
    helpEmbed.add_field(
        name="**__HOW TO CHECK YOUR DATA USAGE__**",
        value="To get a summary of your data usage and data remaining, simple DM '!data' to the ProResiBot depending on which plan you have purchased..\n\nIf you need further assistance, please check our [#guide](LINK HERE) or [#open-a-ticket](LINK HERE).",
        inline=False
        )
    helpEmbed.set_footer(
        text="CompanyName. All rights reserved.",
        icon_url="COMPANY LOGO LINK"
    )

    
    await channel.send(embed= helpEmbed)


async def closeUser(orderID,userD):


    try:
        config = {
        "apiKey": "API KEY",
        "authDomain": ".firebaseapp.com",
        "databaseURL": "YOUR DATABASE URL",
        "storageBucket": ".appspot.com",
        "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
        }

        firebase = pyrebase.initialize_app(config)
        orders = []
        db = firebase.database()
        inventory = db.child('orders').get()
        # gets json data of all orders (this might need changed in fture if we have too many orders)
        for order in inventory.each():
            orders.append(order.val())
        for order in orders:
            if orderID in order["PlanDetails"]["Order ID"]:
                if order['Status'] == 'Active':
                    Pdetails = {
                    'Available': 0
                    }
                    db.child('orders').child(orderID).child('Available').update(Pdetails)

                    Pdetails = {
                    'Status': 'Closed'
                    }
                    db.child('orders').child(orderID).child('Status').update(Pdetails)
                    user = client.get_user(userD)

                    dataEmbed = Embed(
                        title=f"CompanyName",
                        colour=0x9400D3,
                        url="https://DOMAIN.HERE",
                    )
                    dataEmbed.add_field(
                        name="PLAN EXPIRED",
                        value="Your plan has run out of data. If you require a new one, please visit https://DOMAIN.HERE/",
                        inline=False
                        )

                    dataEmbed.set_footer(
                        text="CompanyName. All rights reserved.",
                        icon_url="COMPANY LOGO LINK"
                    )

                    
                    user = client.get_user(userD)
                    await user.send(embed=dataEmbed)

                    
                else:
                    pass
            else:
                pass

    except Exception as e:
        print(e)
        return on_ready()


async def checkSmart(orderID,userD):

    try:


        session = requests.session()

        url = "https://api.smartproxy.com/v1/auth"

        headers = {"Authorization": "Basic TOKEN HERE"}

        response = session.post(url, headers=headers)
        SmartuserID = response.json()['user_id']
        authToken = response.json()['token']

        url = f"https://api.smartproxy.com/v1/users/{SmartuserID}/sub-users"

        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Token {authToken}"
                }

        r = session.get(url, headers=headers)

        for subUser in r.json():
            if subUser["traffic"] != 0:
                totalUsed = subUser['traffic']   
                totalBought = subUser['traffic_limit'] 
                customerID = subUser['id']
                dataLeft = totalBought - totalUsed

                if dataLeft <= 0:
                    await closeUser(orderID,userD)


                    url = f"https://api.smartproxy.com/v1/users/{SmartuserID}/sub-users/{str(customerID)}"

                    headers = {
                                "Content-Type": "application/json",
                                "Authorization": f"Token {authToken}"
                            }

                    r = session.delete(url, headers=headers)
                    print(r.text)
                else:
                    pass
               
                
            else:
                pass
    
    except Exception as e:
        print(e)
        return on_ready()

        


async def checker():
    print('starting checker')


    config = {
            "apiKey": "API KEY",
            "authDomain": ".firebaseapp.com",
            "databaseURL": "YOUR DATABASE URL",
            "storageBucket": ".appspot.com",
            "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
        }

    firebase = pyrebase.initialize_app(config)
    orders = []
    logins = []
    accToCheck = []
    db = firebase.database()
    inventory = db.child('orders').get()
    Userlogins = db.child('Active Logins').get()
    # gets json data of all orders (this might need changed in fture if we have too many orders)
    for logg in Userlogins.each():
        logins.append(logg.val())
    for order in inventory.each():
        orders.append(order.val())

    for login in logins:
        accToCheck.append(login['Order ID'])
    for orderr in orders:
        for logs in accToCheck:
            if str(logs) in str(orderr["PlanDetails"]["Order ID"]):
                if orderr['Status'] == 'Active':
                    proxyDeets = orderr['PlanDetails']
                    Pplan = proxyDeets['type']
                    orderID = proxyDeets['Order ID']
                    userD = proxyDeets['Discord ID']
                    
                    # variables are set and discord user ID is validated 
                  
                    if "BP" in Pplan:
                        pass
                    else:
                        await checkSmart(orderID,userD)
                    


async def getdataLeft(Pplan,userID,message):
    channel = message.channel
    session = requests.session()
    if 'PP' in Pplan:

        session = requests.session()

        url = "https://api.smartproxy.com/v1/auth"

        headers = {"Authorization": "Basic TOKEN HERE"}

        response = session.post(url, headers=headers)
        SmartuserID = response.json()['user_id']
        authToken = response.json()['token']

        url = f"https://api.smartproxy.com/v1/users/{SmartuserID}/sub-users"

        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Token {authToken}"
                }

        r = session.get(url, headers=headers)

        for subUser in r.json():
            if subUser["username"] == userID:
                subuserID = subUser['id']
                totalUsed = subUser['traffic']   
                totalBought = subUser['traffic_limit'] 
                totalDataLeft = totalBought - totalUsed
        
        url = f"https://api.smartproxy.com/v1/users/{SmartuserID}/sub-users/{str(subuserID)}/traffic"

        params = {
            'type':'24h'
        }

        headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Token {authToken}"
                }

        r = session.get(url, headers=headers, params = params)
        page = r.json()
        dayUsage = page['traffic']

        params = {
            'type':'7days'
        }

        r = session.get(url, headers=headers, params = params)
        weekUsage = r.json()['traffic']

        params = {
            'type':'month'
        }

        r = session.get(url, headers=headers, params = params)
        monthUsage = r.json()['traffic']

       
        return totalDataLeft, dayUsage, weekUsage, monthUsage, totalUsed


async def getMessages(message):

    global channel
    channel = message.channel
    mess = message.content
 
    login = mess.split(' ')

    if isinstance(message.channel, discord.channel.DMChannel):
  
        try:
            username = login[1]
        except:
            errorEmbed = await embedErrorGen("Error reading username, please check and try again")
            await channel.send(embed= errorEmbed)
            await on_ready()
        
        
        try:
            password = login[2]
        except:
            errorEmbed = await embedErrorGen("Error reading password, please check and try again")
            await channel.send(embed= errorEmbed)
            await on_ready()
        

        config = {
            "apiKey": "API KEY",
            "authDomain": ".firebaseapp.com",
            "databaseURL": "YOUR DATABASE URL",
            "storageBucket": ".appspot.com",
            "serviceAccount": "SERVICE ACCOUNT FILE LINK.json"
            }

        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        global user_exists
        user_exists = False
        orders = []
        # connects to database and gets all order data
        inventory = db.child('orders').get()
        for order in inventory.each():
            orders.append(order.val()) 
        
        for order in orders:
            proxyDeets = order['PlanDetails']
            # Validates username and password entered by users (user gets this from email) matches ones stores in our databse
            if username == proxyDeets['loginUsername']:
                if password == proxyDeets['loginPassword']:
                    # If they match, we tell them they have logged in, we get their discord name and add that to proxydetails in our database and is used for validation later
                    print(f'user {username} logged in')
                    successEmbed = Embed(
                        title=f"CompanyName",
                        colour=0x9400D3,
                        url="https://DOMAIN.HERE",
                    )
                    successEmbed.add_field(
                        name="LOGGED IN",
                        value=f"You have logged into plan with username {username},\n**Welcome to CompanyName** ",
                        inline=False
                        )

                    successEmbed.set_footer(
                        text="CompanyName. All rights reserved.",
                        icon_url="COMPANY LOGO LINK"
                    )
                    
                    await channel.send(embed=successEmbed)
                    orderID = proxyDeets['Order ID']
                    user = str(message.author.id).replace('#','')

                    Pdetails = {
                    'Discord ID': user
                    }
                    db.child('orders').child(orderID).child('PlanDetails').update(Pdetails)

                    loginDetails = {
                        'Discord ID': user,
                        'Order ID': orderID
                    }

                    db.child('Active Logins').child(user).update(loginDetails)


                    user_exists = True
                    break

                else:
                    errorEmbed = await embedErrorGen("Error logging in, please check details and try again")
                    await channel.send(embed= errorEmbed)
                    await on_ready()

            else:
                pass



@client.event
async def on_message(message):
    print(client)
    if message.content.startswith(prefix):
        cmd = message.content.lstrip(prefix).split(' ')[0]
        if cmd == "login":
            await getMessages(message)
        elif cmd == "data":
            await fetchData(message)
        elif cmd == "help":
            await helpMessage(message)
        elif cmd == "gen":
            await genProxies(message)
        elif cmd == "generate":
            await genProxies(message)
        elif cmd == "fast":
            await fastGen(message)
        elif cmd == "QR":
            await polarGen(message)
        elif cmd == "checkplans":
            onlyUs = ["STAFFE DISCORD ID'S HERE"]
            userD = str(message.author.id)
            if userD not in onlyUs:
                pass
            else:
                await checker()

client.run(token)
# Starts the bot.
