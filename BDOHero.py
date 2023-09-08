import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time
import random
import selenium
import requests
import io
from selenium import webdriver
from bs4 import BeautifulSoup
import base64

Client = discord.Client()
bot = commands.Bot(command_prefix = "-")

minutes = 0
hour = 0

@bot.event
async def on_ready():
	print ("Bot is online and connected to discord!")
	await bot.change_presence(game = discord.Game(name = "with your Soul"))

@bot.event
async def on_message(message):
	if message.content.upper().startswith('-PING'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s> Pong!" % (userID))
	if message.content.upper().startswith('FUCK YOU'):
		args = message.content.split(" ")
		await bot.send_message(message.channel, '%s :middle_finger:' % (" ".join(args[2:])))
		await bot.delete_message(message)
	if message.content.upper().startswith('-LISTGEAR'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s> Now Parsing..." % (userID))
		args = message.content.split(" ")
		url = '%s' % (args[1])
		driver = webdriver.Chrome()

		driver.get(url)
		innerHTML = driver.execute_script("return document.body.innerHTML")

		soup = BeautifulSoup(innerHTML, 'html.parser')
		yourclass = soup.find('span', attrs = {'class':'current-class'})
		gearlist = soup.find('ul', attrs = {'id':'gear-list'})
		enhstats = soup.find('ul', attrs = {'class':'stats ench-stats'})
		exdstats = soup.find('ul', attrs = {'class':'stats extra-stats'})
		offstats = soup.find('ul', attrs = {'class':'stats offence-stats'})
		defstats = soup.find('ul', attrs = {'class':'stats defense-stats'})
		resstats = soup.find('ul', attrs = {'class':'stats resist-stats'})
		lifstats = soup.find('ul', attrs = {'class':'stats survive-stats'})
		genstats = soup.find('ul', attrs = {'class':'stats general-stats'})
		gspstats = soup.find('ul', attrs = {'class':'stats special-stats'})
		pristats = soup.find('table', attrs = {'class':'stats-table'})
		gearscore = soup.find('div', attrs = {'id':'gear-score'})
		gearscore1 = gearscore.find('span', attrs = {'class':'value'})

		content = []	
		content.append('----------------------------------------------')
		content.append('Current Class:')
		content.append(yourclass.text)
		content.append('----------------------------------------------')
		content.append('----------------------------------------------')
		content.append('Gear List:')
		for row in gearlist.findAll('li'):
			content.append(row.contents[0])
		content.append('----------------------------------------------')
		content.append('----------------------------------------------')
		content.append('Primary Stats:')
		for row in pristats.findAll('td'):
			content.append(row.text)
		content.append('Gear Score')
		content.append(gearscore1.text)
		content.append('----------------------------------------------')
		await bot.send_message(message.channel,"\n".join(content))
		driver.quit() 
		await bot.delete_message(message)
	if message.content.upper().startswith('-STATBOOST'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s> Now Parsing..." % (userID))
		args = message.content.split(" ")
		url = '%s' % (args[1])
		driver = webdriver.Chrome()

		driver.get(url)
		innerHTML = driver.execute_script("return document.body.innerHTML")

		soup = BeautifulSoup(innerHTML, 'html.parser')
		yourclass = soup.find('span', attrs = {'class':'current-class'})
		gearlist = soup.find('ul', attrs = {'id':'gear-list'})
		enhstats = soup.find('ul', attrs = {'class':'stats ench-stats'})
		exdstats = soup.find('ul', attrs = {'class':'stats extra-stats'})
		offstats = soup.find('ul', attrs = {'class':'stats offence-stats'})
		defstats = soup.find('ul', attrs = {'class':'stats defense-stats'})
		resstats = soup.find('ul', attrs = {'class':'stats resist-stats'})
		lifstats = soup.find('ul', attrs = {'class':'stats survive-stats'})
		genstats = soup.find('ul', attrs = {'class':'stats general-stats'})
		gspstats = soup.find('ul', attrs = {'class':'stats special-stats'})
		pristats = soup.find('table', attrs = {'class':'stats-table'})
		gearscore = soup.find('div', attrs = {'id':'gear-score'})
		gearscore1 = gearscore.find('span', attrs = {'class':'value'})

		content = []
		content.append('----------------------------------------------')
		content.append('Stat Boosts (These are IN ADDITION to your character):')
		content.append('----------------------------------------------')
		content.append('Enhancement:')
		for row in enhstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('Extra Damage:')
		for row in exdstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('Offensive:')
		for row in offstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('Defensive:')
		for row in defstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('Resistance:')
		for row in resstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('Survivability:')
		for row in lifstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('General:')
		for row in genstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')
		content.append('Gear Specials:')
		for row in gspstats.findAll('li'):
			content.append(row.text)
		content.append('----------------------------------------------')

		await bot.send_message(message.channel,"\n".join(content))
		driver.quit()
		await bot.delete_message(message)
	if message.content.upper().startswith('-SAY'):
		args = message.content.split(" ")
		await bot.send_message(message.channel, "%s" % (" ".join(args[1:])))
		await bot.delete_message(message)
	if message.content.upper().startswith('-COOKIE'):
		await bot.send_message(message.channel, ":cookie:")
		await bot.delete_message(message)
	if message.content.upper().startswith('WHAT CLASS IS CALEB'):
		await bot.send_message(message.channel,
		 "Hmmm... Maybe %s" % (random.choice(['Warrior','Sorceress','Ranger... Again','Berserker... for the next hour','Tamer','Musa','Maehwa','Valkyrie','Wizard','Witch','Ninja','Kunoichi','Dark Knight','Striker','he turned to Mystic trash'])))
	if message.content.upper().startswith('-GEAR'):
		if '@' in message.content:
			try:
				args = message.content.split(" ")
				userID = args[1]
				userIDstripped = userID.translate(str.maketrans('', '', '<' + '!' + '>'))
				file = open(r'C:\Users\hough\OneDrive\Desktop\BotTest\links' + '\%s.txt' % (userIDstripped), "r")
				contents = file.read()
				link_start_ind = 0
				for i in range(0, len(contents)):
				    if contents[i:i + 8] == '\'url\': \'':
				        link_start_ind = i + 8
				        break
				link_end_ind = 0
				for i in range(link_start_ind, len(contents)):
				    link_end_ind = i
				    if contents[i] == '\'':
				        break
				await bot.send_message(message.channel, contents[link_start_ind:link_end_ind])
			except:
				await bot.send_message(message.channel, "No Data On This User")
		else:
			userID = message.author.id
			file = open(r"C:\Users\hough\OneDrive\Desktop\BotTest\links" + "\@%s.txt" % (userID), "w+")
			read = r"C:\Users\hough\OneDrive\Desktop\BotTest\links" + "\@%s.txt" % (userID)
			image = message.attachments
			if os.path.exists(read):
				open(read).close()
			file.write('%s' % (image))
			await bot.send_message(message.channel, '<@%s> Image Saved.' % (userID))
	if message.content.upper().startswith('-UPTIME'):
		await bot.send_message(message.channel, 
			"I have been online for:\n {0} hours\n {1} minutes\n on {2}".format(hour, minutes, message.server))
	if message.content.upper().startswith('-HELP'):
		userID = message.author.id
		await bot.send_message(message.channel, '<@%s>' % (userID))
		generalembed = discord.Embed(
			title="__General:__",
			description=' **-help**\n       *Command List*\n **-ping**\n       *Ping the Bot*\n **-say <Insert Anything Here>**\n      *Make BDO Hero Say Something*\n **-cookie**\n       *Everyone Likes Cookies*\n **-uptime**\n       *Get Information On BDO Hero Uptime*\n **-links**\n       *Useful Links, Usually Related to BDO*\n **-coin**\n       *Sometimes a Coin Flip is the Only Solution*\n **-user <@mention_someone>**\n       *Learn Everyhing ( ͡° ͜ʖ ͡°)*\n **-kill<@mention_someone>**\n       *Whoah There Calm Down Now*\n **-image [Attach Image Here]**\n       *Saves an Image to Your User*\n **-image <@mention_someone>**\n       *Sends A Users Image*\n\nRmluZCBTZWNyZXQgQ29tbWFuZHMgV2l0aCBMV2hwWkdSbGJnPT0=',
			color=0x2ac12a
		)
		generalembed.set_author(
			name="Command List"
		)
		await bot.send_message(message.channel, embed=generalembed)
		BDOembed = discord.Embed(
			title="__BDO Related Commands:__",
			description=' **-gear [Attach Image Here]**\n       *Saves Your Gear Image*\n **-gear <@mention_someone>**\n       *View Someones Gear Image*\n **-listgear [Send BDO Planner Link]**\n       *List All The Gear From Your Link*\n **-stats [Send BDO Planner Link]**\n       *List All The Stat Bonuses Given By The Gear*',
			color=0xb12ac1
		)
		await bot.send_message(message.channel, embed=BDOembed)
	if message.content.upper().startswith('-HIDDEN'):
		userID = message.author.id
		await bot.delete_message(message)
		await bot.send_message(message.channel, '***YOU SAW NOTHING!***')
		hiddenembed = discord.Embed(
			title="__Hidden General Commands:__",
			description=' **-hidden**\n       *It is Hidden, How Would I Know What It Does*\n **fuck you <Any Text Here>**\n        *Sometimes A Little Hatred Goes A Long Way*\n **what class is caleb**\n       *I Dont Know, You Tell Me*\n **-sourcecode**\n       *Sends a Github Gist Where I Store All My Code*',
			color=0xFFFFFF
		)
		hiddenembed.set_author(
			name="Congrats! You Found the Secret Commands!"
		)
		voiceembed = discord.Embed(
			title="__Commands For When You Are In A Voice Channel:__",
			description=' **-ree**\n       *You Need At Least Two E`s, But More Will Work*\n **-urmomgae**\n       *What. She Is, I Am Just Stating Facts*',
			color=0x165792
		)
		await bot.send_message(message.author, embed=hiddenembed)
		await bot.send_message(message.author, embed=voiceembed)
	if message.content.upper().startswith('-LINKS'):
		userID = message.author.id
		linkembed = discord.Embed(
			title="__Useful Links:__",
			description=' **-recipe**\n       *A BDO Cooking Recipe Website*\n **-enhance**\n       *A BDO Enhancement Simulator*',
			color=0x165792
		)
		await bot.send_message(message.channel, '<@%s>' % (userID))
		await bot.send_message(message.channel, embed=linkembed)
	if message.content.upper().startswith('-COIN'):
		choice = random.randint(1,2)
		if choice == 1:
			await bot.send_message(message.channel, 'HEADS!')
		if choice == 2:
			await bot.send_message(message.channel, 'TAILS!')
	if message.content.upper().startswith('***YOU SAW NOTHING!***'):
		time.sleep(0.45)
		await bot.delete_message(message)
	if message.content.upper().startswith('-USER'):
	        try:
	            user = message.mentions[0]
	            userjoinedat = str(user.joined_at).split('.', 1)[0]
	            usercreatedat = str(user.created_at).split('.', 1)[0]
	 
	            userembed = discord.Embed(
	                title="Username:",
	                description=user.name,
	                color=0xe67e22
	            )
	            userembed.set_author(
	                name="User Info"
	            )
	            userembed.add_field(
	                name="Joined the server at:",
	                value=userjoinedat
	            )
	            userembed.add_field(
	                name="User Created at:",
	                value=usercreatedat
	            )
	            userembed.add_field(
	                name="Discriminator:",
	                value=user.discriminator
	            )
	            userembed.add_field(
	                name="User ID:",
	                value=user.id
	            )
	 
	            await bot.send_message(message.channel, embed=userembed)
	        except IndexError:
	            await bot.send_message(message.channel, "User Not Found.")
	        except:
	            await bot.send_message(message.channel, "Error.")
	        finally:
	            pass
	if message.content.upper().startswith('-KILL'):
		args = message.content.split(" ")
		userID = message.author.id
		await bot.send_message(message.channel, 'HOLY CRAP! %s ' % (args[1]) + 'was %s by ' % (random.choice(['murdered', 'killed', 'slaughtered', 'annihilated', 'massacred', 'slain', 'butchered'])) + '%s ' % (random.choice(['being loved to death', 'getting stabbed', 'getting 360 no-scoped', 'having boiling water poured into their brain', 'being forced to reroll Mystic', 'being decapitated'])) + 'by <@%s>' % (userID))
		await bot.delete_message(message)
	if message.content.upper().startswith('-IMAGE'):
		if '@' in message.content:
			try:
				args = message.content.split(" ")
				userID = args[1]
				userIDstripped = userID.translate(str.maketrans('', '', '<' + '!' + '>'))
				file = open(r'C:\Users\hough\OneDrive\Desktop\BotTest\images' + '\%s.txt' % (userIDstripped), "r")
				contents = file.read()
				link_start_ind = 0
				for i in range(0, len(contents)):
				    if contents[i:i + 8] == '\'url\': \'':
				        link_start_ind = i + 8
				        break
				link_end_ind = 0
				for i in range(link_start_ind, len(contents)):
				    link_end_ind = i
				    if contents[i] == '\'':
				        break
				await bot.send_message(message.channel, contents[link_start_ind:link_end_ind])
			except:
				await bot.send_message(message.channel, "No Data On This User")
		else:
			userID = message.author.id
			file = open(r"C:\Users\hough\OneDrive\Desktop\BotTest\images" + "\@%s.txt" % (userID), "w+")
			read = r"C:\Users\hough\OneDrive\Desktop\BotTest\images" + "\@%s.txt" % (userID)
			image = message.attachments
			if os.path.exists(read):
				open(read).close()
			file.write('%s' % (image))
			await bot.send_message(message.channel, '<@%s> Image Saved.' % (userID))
	if message.content.upper().startswith('-REE'):
		try:
			await bot.delete_message(message)
			channel = message.author.voice.voice_channel
			vc = await bot.join_voice_channel(channel)
			player = vc.create_ffmpeg_player(r'C:\Users\hough\OneDrive\Desktop\BotTest\sounds\reesoundeffect.mp3')
			player.start()
			time.sleep(6)
			await vc.disconnect()
		except:
			await bot.send_message(message.channel, 'Error')
	if message.content.upper().startswith('-URMUMGAE'):
		try:
			await bot.delete_message(message)
			channel = message.author.voice.voice_channel
			vc = await bot.join_voice_channel(channel)
			player = vc.create_ffmpeg_player(r'C:\Users\hough\OneDrive\Desktop\BotTest\sounds\urmumgae.mp3')
			player.start()
			time.sleep(3)
			await vc.disconnect()
		except:
			await bot.send_message(message.channel, 'Error')
	if message.content.upper().startswith('-OHMYGOD'):
		try:
			await bot.delete_message(message)
			channel = message.author.voice.voice_channel
			vc = await bot.join_voice_channel(channel)
			player = vc.create_ffmpeg_player(r'C:\Users\hough\OneDrive\Desktop\BotTest\sounds\ohmygod.mp3')
			player.start()
			time.sleep(5)
			await vc.disconnect()
		except:
			await bot.send_message(message.channel, 'Error')
	if message.content.upper().startswith('-SOURCECODE'):
		await bot.delete_message(message)
		await bot.send_message(message.author, 'Not Totally Sure Why You Would Want This,\nBut Here You Go:\nhttps://gist.github.com/HeroicosHM/1f52fab50729b699934dfcf3ce1d81b5')
	if message.content.upper().startswith('-LENNY'):
		await bot.delete_message(message)
		await bot.send_message(message.channel, "%s" % (random.choice(['( ͡° ͜ʖ ͡°)','(☭ ͜ʖ ☭)','(⟃ ͜ʖ ⟄) ','( ͡◉ ͜ʖ ͡◉)','( ͡☉ ͜ʖ ͡☉)','━╤デ╦︻(▀̿̿Ĺ̯̿̿▀̿ ̿)','༼(∩ ͡°╭͜ʖ╮͡ ͡°)༽⊃━☆ﾟ. * ･ ｡ﾟ',
			'(ง ͠° ͟ل͜ ͡°)ง[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]','╭∩╮( ͡° ل͟ ͡° )╭∩╮','┬┴┬┴┤ᕦ( ▀̿ Ĺ̯ ▀̿├┬┴┬','( ° ͜ʖ͡°)╭∩╮','( ͡⚆ ͜ʖ ͡⚆)╭∩╮','(˵ ͡~ ͜ʖ ͡°˵)ﾉ⌒♡*:･。.','( ˶˘ ³˘(˵ ͡° ͜ʖ ͡°˵)♡','( ͡☉⁄ ⁄ ͜⁄ ͜ʖ̫⁄ ⁄ ͡☉)',
			'(つ ♥灬 ͜ʖ 灬♥)つ','(˵ ͡° ͜ʖ ͡°˵)','(♥ ͡° ͜ʖ ͡°)','┬┴┤( ͡⚆ل͜├┬┴┬'])))
	if message.content.upper().startswith('-RECIPE'):
		try:
			userID = message.author.id
			file = open(r'C:\Users\hough\OneDrive\Desktop\BotTest\BDOInfo\recipecalc.txt', "r")
			contents = file.read()
			link_start_ind = 0
			for i in range(0, len(contents)):
			    if contents[i:i + 8] == '\'url\': \'':
			        link_start_ind = i + 8
			        break
			link_end_ind = 0
			for i in range(link_start_ind, len(contents)):
			    link_end_ind = i
			    if contents[i] == '\'':
			        break
			await bot.send_message(message.channel, '<@%s>\n' % (userID) + 'This webste allows you to see all cooking recipes in BDO:\n' + contents[link_start_ind:link_end_ind])
		except:
			await bot.send_message(message.channel, "No Data")
	if message.content.upper().startswith('-ENHANCE'):
		try:
			userID = message.author.id
			file = open(r'C:\Users\hough\OneDrive\Desktop\BotTest\BDOInfo\enhancesim.txt', "r")
			contents = file.read()
			link_start_ind = 0
			for i in range(0, len(contents)):
			    if contents[i:i + 8] == '\'url\': \'':
			        link_start_ind = i + 8
			        break
			link_end_ind = 0
			for i in range(link_start_ind, len(contents)):
			    link_end_ind = i
			    if contents[i] == '\'':
			        break
			await bot.send_message(message.channel, '<@%s>\n' % (userID) + 'This webste simulate whats enhancing is like in BDO:\n' + contents[link_start_ind:link_end_ind] + '\nDisclaimer: This website is new and relatively under-developed.')
		except:
			await bot.send_message(message.channel, "No Data")
	if message.content.upper().startswith('-BASE64'):
		args = message.content.split(" ")
		userID = message.author.id
		code = args[1]
		decoded = base64.b64decode(code)
		decodedproper = decoded.decode("utf-8")
		await bot.send_message(message.channel, '<@%s>\n' % (userID) + decodedproper)
	if message.content.upper().startswith('-ENCODEBASE64'):
		userID = message.author.id
		args = message.content.split(" ")
		encode = args[1:]
		encoded = base64.b64encode(encode)
		await bot.send_message(message.channel, '<@%s>\n' % (userID) + encoded)
	if 'Image Saved.' in message.content:
		time.sleep(5)
		await bot.delete_message(message)		
	if message.content.upper().startswith('-TANA'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%S>\nWHOAH! Check Out Tana's Awesome Website!!!\nhttp://dndmonsterhunter.com/" % (userID))
	if message.content.upper().startswith('-HERO'):
		userID = message.suthor.id
		await bot.send_message(message.channel, '<@%s>\nYou know, I Hear He Is An Awesome Dude.' % (userID))
	if message.content.upper().startswith('-AURO'):
		userID = message.author.id
		await bot.send_message(message.channel, '<@%s>\nAurorans Is The Single Most Rusty Boy I Have Ever Met' % (userID))
	if message.content.upper().startswith('-VOR'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s>\nLet Me Tell You A Story:\nVorsent Is Daddy.\nEnd Of Story." % (userID))
	if message.content.upper().startswith('-CORGI'):
		userID = message.author.id
		await bot.send_message(message.channel, '<@%s>\nHow Many Corgies Are There?\nThe World May Never Know...' % (userID))
	if message.content.upper().startswith('-ROOMBA'):
		userID = message.author.id
		await bot.send_message(message.channel, '<@%s>\nWhat Does The Roomba Say?\nRREEEEEEEEEE' % (userID))
	if message.content.upper().startswith('-JUAN'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s>\nJuan Is..." % (userID))
		time.sleep(1.5)
		await bot.send_message(message.channel, "Well Let's Just Say That Juan Will Be Juan.")
	if message.content.upper().startswith('-CRIM'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s>\nWho Even Is This CrimsonTitain Dude?" % (userID))
	if message.content.upper().startswith('-CALEB'):
		userID = message.author.id
		msg = await bot.send_message(message.channel, "<@%s>\nCaleb Is A Very Special Child." % (userID))
		time.sleep(0.5)
		await bot.edit_message(msg, "<@%s>\nCaleb Is An Extremely Cool Dude." % (userID))
	if message.content.upper().startswith('-BEN'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s>\nGas Him Or He Will Take Your Money." % (userID))
	if message.content.upper().startswith('-SUSHI'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s>\nHmmmm..." % (userID))
		time.sleep(1.5)
		await bot.send_message(message.channel, "PvP?")
	if message.content.upper().startswith('-BLINKIE'):
		userID = message.author.id
		await bot.send_message(message.channel, "<@%s>\nYou Should Join The Private Server." % (userID))

async def uptime():
	await bot.wait_until_ready()
	global minutes
	minutes = 0
	global hour
	hour = 0
	while not bot.is_closed:
		await asyncio.sleep(60)
		minutes += 1
		if minutes == 60:
			minutes = 0
			hour += 1

@bot.event
async def on_member_join(member):
	serverchannel = member.server.default_channel
	await bot.send_message(serverchannel, "Welcome {0} to {1}".format(member.name, member.server.name))


bot.loop.create_task(uptime())
bot.run("NDIyODQ0MTY4NDAzMTU3MDAy.DYhtvQ.HgZr6CrSBgB2WbpRZNHR9kIekxg")