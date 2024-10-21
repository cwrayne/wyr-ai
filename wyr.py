import time
print("\n--------------------------------\nWould you Rather - AI edition v1\n--------------------------------\n")
time.sleep(2)
print("Initializing...")
import os
pathgame = f"{os.getcwd()}/wyr-ai.txt"
pathgame_file = open(pathgame, mode='w')
from openai import OpenAI
import openai
client = OpenAI(api_key="key")
import socket
import os
def check_internet_connection():
	remote_server = "www.google.com"
	port = 80
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(5)
	try:
		sock.connect((remote_server, port))
		return True
	except socket.error:
		return False
	finally:
		sock.close()
response = ""
def new():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
new()
print("Checking internet connection.")
if check_internet_connection:
	print("Internet connected.")
	time.sleep(0.3)
elif check_internet_connection == False:
	print("No internet connection. Exiting in 3 seconds...")
	time.sleep(3)
	exit()
new()
print("What should the topic of the Would you Rather questions be?")
topic = input("[q] Quit    [enter] Choose    Input: ")
if topic == "q":
	print("Would you like to quit of should the topic be \"q\"?")
	quit_or_topic = input("[q] Quit    [t] Choose Topic    [enter] Continue    Input: ")
	if quit_or_topic == "q":
		print("Quitting...")
		exit()
	elif quit_or_topic == "t":
		print("Chose the topic \"q\".")
		topic == "q"
else:
	print("Set topic to \"" + topic + "\".")
new()
num = 1
print("5 questions will be generated.")
print("2 choices will be generated")
print("Generating question " + str(num) + "...")
time.sleep(5)
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
	{"role": "system", "content": "You are a helpful assistant that writes Would you Rather questions. You will give 2 choices like this: [Choice 1] - [Choice 2] . (no brackets though) Do NOT include the \"Would you Rather\"part. No periods either."},
	{
		"role": "user",
		"content": f"Give me a Would you Rather question about {topic}."
	}
]
)

finishedResponse = completion.choices[0].message.content
print(f"Question {str(num)} recieved. Splitting...")
num1choice1, num1choice2 = finishedResponse.split(' - ')

new()
print(f"Question {str(num)}: Would you rather 1. {num1choice1} or 2. {num1choice2}?")
currentQuestion = input("[enter] Choose   Input: ")
if currentQuestion == "1":
	print(f"Selected #1: {num1choice1} for question {str(num)}.")
	num1choice = 1
elif currentQuestion == "2":
	print(f"Selected #2: {num1choice2} for question {str(num)}.")
	num1choice = 2
num += 1
###
print("Generating question " + str(num) + "...")
time.sleep(5)
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
	{"role": "system", "content": "You are a helpful assistant that writes Would you Rather questions. You will give 2 choices like this: [Choice 1] - [Choice 2] . (no brackets though) Do NOT include the \"Would you Rather\"part. No periods either."},
	{
		"role": "user",
		"content": f"Give me a Would you Rather question about {topic}."
	}
]
)

finishedResponse = completion.choices[0].message.content
print(f"Question {str(num)} recieved. Splitting...")
num2choice1, num2choice2 = finishedResponse.split(' - ')

new()
print(f"Question {str(num)}: Would you rather 1. {num2choice1} or 2. {num2choice2}?")
currentQuestion = input("[enter] Choose   Input: ")
if currentQuestion == "1":
	print(f"Selected #1: {num2choice1} for question {str(num)}.")
	num2choice = 1
elif currentQuestion == "2":
	print(f"Selected #2: {num2choice2} for question {str(num)}.")
	num2choice = 2
num += 1
###
print("Generating question " + str(num) + "...")
time.sleep(5)
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
	{"role": "system", "content": "You are a helpful assistant that writes Would you Rather questions. You will give 2 choices like this: [Choice 1] - [Choice 2] . (no brackets though) Do NOT include the \"Would you Rather\"part. No periods either."},
	{
		"role": "user",
		"content": f"Give me a Would you Rather question about {topic}."
	}
]
)

finishedResponse = completion.choices[0].message.content
print(f"Question {str(num)} recieved. Splitting...")
num3choice1, num3choice2 = finishedResponse.split(' - ')

new()
print(f"Question {str(num)}: Would you rather 1. {num3choice1} or 2. {num3choice2}?")
currentQuestion = input("[enter] Choose   Input: ")
if currentQuestion == "1":
	print(f"Selected #1: {num3choice1} for question {str(num)}.")
	num3choice = 1
elif currentQuestion == "2":
	print(f"Selected #2: {num3choice2} for question {str(num)}.")
	num3choice = 2
num += 1
###
print("Generating question " + str(num) + "...")
time.sleep(5)
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
	{"role": "system", "content": "You are a helpful assistant that writes Would you Rather questions. You will give 2 choices like this: [Choice 1] - [Choice 2] . (no brackets though) Do NOT include the \"Would you Rather\"part. No periods either."},
	{
		"role": "user",
		"content": f"Give me a Would you Rather question about {topic}."
	}
]
)

finishedResponse = completion.choices[0].message.content
print(f"Question {str(num)} recieved. Splitting...")
num4choice1, num4choice2 = finishedResponse.split(' - ')

new()
print(f"Question {str(num)}: Would you rather 1. {num4choice1} or 2. {num4choice2}?")
currentQuestion = input("[enter] Choose   Input: ")
if currentQuestion == "1":
	print(f"Selected #1: {num4choice1} for question {str(num)}.")
	num4choice = 1
elif currentQuestion == "2":
	print(f"Selected #2: {num4choice2} for question {str(num)}.")
	num4choice = 2
num += 1
###
print("Generating question " + str(num) + "...")
time.sleep(5)
completion = client.chat.completions.create(
model="gpt-4o-mini",
messages=[
	{"role": "system", "content": "You are a helpful assistant that writes Would you Rather questions. You will give 2 choices like this: [Choice 1] - [Choice 2] . (no brackets though) Do NOT include the \"Would you Rather\"part. No periods either."},
	{
		"role": "user",
		"content": f"Give me a Would you Rather question about {topic}."
	}
]
)

finishedResponse = completion.choices[0].message.content
print(f"Question {str(num)} recieved. Splitting...")
num5choice1, num5choice2 = finishedResponse.split(' - ')

new()
print(f"Question {str(num)}: Would you rather 1. {num5choice1} or 2. {num5choice2}?")
currentQuestion = input("[enter] Choose   Input: ")
if currentQuestion == "1":
	print(f"Selected #1: {num5choice1} for question {str(num)}.")
	num5choice = 1
elif currentQuestion == "2":
	print(f"Selected #2: {num5choice2} for question {str(num)}.")
	num5choice = 2
num += 1
###
new()
#Summary
print("-------\nSummary\n-------")
print(f"Question 1: Would you rather {num1choice1} or {num1choice2}? You picked #{str(num1choice)}")
print(f"Question 2: Would you rather {num2choice1} or {num2choice2}? You picked #{str(num2choice)}")
print(f"Question 3: Would you rather {num3choice1} or {num3choice2}? You picked #{str(num3choice)}")
print(f"Question 4: Would you rather {num4choice1} or {num4choice2}?. You picked #{str(num4choice)}")
print(f"Question 5: Would you rather {num5choice1} or {num5choice2}?. You picked #{str(num5choice)}")

print("Would you like to save your game to a text file  (y/n)?\n")
save = input("[q] Quit   [enter] Choose   Input: ")
if save == "y":
	print("Input path (nothing for <current path>/wyr-ai.txt, will overwrite current game!)\n")
	path = input("[q] Quit   [enter] Choose   Input: ")
	if path == "":
		print(f"Set path to {pathgame}")
	else:
		print(f"Set path to {path}.")
	pathgame_file.write(f"Would You Rather Game \n\n Question 1: \"Would you rather {num1choice1} or {num1choice2}?\" \nYou picked #{num1choice}. \n\n Question 2: \"Would you rather {num2choice1} or {num2choice2}?\" \nYou picked #{num2choice}. \n\n Question 3: \"Would you rather {num3choice1} or {num3choice2}?\" \nYou picked #{num3choice}. \n\n Question 4: \"Would you rather {num4choice1} or {num4choice2}?\" \nYou picked #{num4choice}. \n\n Question 5: \"Would you rather {num5choice1} or {num5choice2}?\" \nYou picked #{num5choice}.")
	pathgame_file.close()
	
if save == "n" or save == "q":
	print("Exiting in 1 second...")
	time.sleep(1)
	exit()
