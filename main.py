#Intro part
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Welcome to Sleep Analyser !")
print()
print(
 "Our aim is to extract the best out of data analytic powers of python from the basics!"
)
print("Your Sleep analysis in the simplest way possible.")
print()
print(
 "NOTE: Our data is not 100% accurate. User's discretion is advised, refer to bibliography for research sources."
)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
Cont = input("Press RETURN to continue...")
print()
#Lets begin
name = str(input("My name is: "))
age = int(input("My age is: "))

#Data analytics
score = 0
print()
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Hello ", name, "!")
print()
print("Please provide sleep data in this format:")
print("       <Hours>:<Minutes> Eg. 8:30")
print()
#Sleep data is converted from string to useful info in simple steps.
sleepdataa = str(input("Yesterday, I went to bed at: "))
sleepdata = list(sleepdataa.partition(":"))
sleepdata.remove(":")
sleephr, sleepmin = 0, 0
sleephr, sleepmin = sleepdata
sleephr = int(sleephr)
sleepmin = int(sleepmin)

#Wake data, saved similiar to sleepdata
wakedataa = str(input("Today, I woke up at: "))
wakedata = list(wakedataa.partition(":"))
wakedata.remove(":")
wakehr, wakemin = 0, 0
wakehr, wakemin = wakedata
wakehr = int(wakehr)
wakemin = int(wakemin)

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print("Analysing Data... [=====================] 100%")
print("Creating Report... [=====================] 100%")

#Total Sleep data
timemid = 11 - sleephr
timemin = 1 - (sleepmin / 60)
timemid = timemin + timemid
timeslept_total = timemid + wakehr + (wakemin / 60)
hrslept = int(timeslept_total)
minslept = int((timeslept_total % 1) * 60)

#Deep and normal sleep
deepsleep_min = int((3 / 10) * (timeslept_total * 60))
lightsleep_min = int((7 / 10) * (timeslept_total * 60))
print('\n' * 1)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("    ", name, "'s Sleep Analysis-")
print()
print("Total time slept: ", hrslept, "hr(s) and", minslept, "min(s)")
print("Deep sleep: ", deepsleep_min, " minute(s)")
print("Light sleep: ", lightsleep_min, " minute(s)")
print()
print("Some useful peices of information and suggestions:")
print()

#THE MAIN ANALYTICS BEGIN..
#place where the magic happens...
#Factor for sleeps score #1 (Hours slept)
if age < 18:
	if hrslept < 8:
		print("• You didnt had sufficient sleep last night!")
		print(">> Your age group must have 8-10 hours of sleep.")
		score -= 10
	if hrslept >= 8 and hrslept <= 10:
		print("• You had sufficient sleep!")
		score += 20
	if hrslept > 10:
		print("• You slep more than it is reqired!")
		print(">> people of your age group must have around 8-10 hours of sleep.")
		score -= 10
else:
	if hrslept < 7:
		print("• You didnt had sufficient sleep last night!")
		print(">> Your age group must have atleast 7 hours of sleep everyday.")
		score -= 10
	if hrslept >= 7 and hrslept <= 9:
		print("• You had sufficient sleep!")
		score += 20

#Factor for sleeps score #2 (Sleep time)
if sleephr > 10:
	print("• You went to bed at an unideal time!")
	print(">> You should try to sleep before 10 O' clock.")
	score -= 10
else:
	print("• Bravo, You slept at the absolutely perfect time!")
	score += 20

#Factor for sleeps score #3 (Sleep time)
if wakehr > 9:
	print("• You woke up at an unideal time!")
	print(">> You should try wakeing up before 9 O' clock.")
	score -= 10
else:
	print("• Bravo, You woke up at the absolutely perfect time!")
	score += 20

#Sleep score print
print()
print("Sleep Score: ", score, "/60")
if score >= 40:
	print("Sleep Quality: Great!")
	print(">>> You must be feeling energetic and active!")
elif score < 40 and score > 20:
	print("Sleep Quality: Good")
	print(">>> You must be feeling active!")
else:
	print("Sleep Quality: Poor")
	print(">>> Feeling sleepy/dizzy? I guess we know why..")
	print(">>> Follow the suggestions for a better sleep experience.")
print()
print("REMINDER: Our data is not 100% accurate. User's discretion is advised, refer to bibliography for research sources.")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
close = input("Press RETURN to close...")

print('\n' * 2)
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Closing the programme now.")
print()
print("Hope you had a great time with our project. ")
print(
 "A quote from the team \"A good laugh and sound sleep are the best cures in a doctor's book\" :) "
)
print("")
print("Submitted by: Lakshya Walia, Aapra Sharma and Mitaksh Goswami.")
print('\n' * 2)
Cont = input("Press RETURN to confrm...")
