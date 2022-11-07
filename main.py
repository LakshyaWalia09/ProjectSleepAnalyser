#Pre load sequence. This include libraries used in this project and other stuff.
from colored import fg, bg, attr


#Main Code begins.
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Welcome to the Project Health BETA")
print("")
print("Your one stop for everything you need to stay healthy in an easy and friendly way!")
print("")
print("NOTE: Our data is not 100% accurate hence cannot be used for regular health checkup we strongly recommend reaching physician for any medical difficulty this tool is just made for fun and educational purposes. ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" ") 
Cont=input("Press RETURN to continue...")
print(" ") 
print(" ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" ")
print("Please choose a service by entering the number of index:-")
print(" ")
print("1] Meditation session")
print("      Take a deep breath and begin your day with a yoga session!")
print(" ")
print("2] Sleep score calculator")
print("      Feeling dizzy? Lets figure out why!")
print(" ")
print("3] Health analyser BETA")
print("      Feeling unhealthy? Take a simple health checkup to know what maybe the reason!")
print(" ")
print("4] Water reminder.")
print("      Feeling like a warm day or just like you are gonna miss the minimum drinking requirement, We got you cover!")
print(" ")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("")
opt=input("I choose: ")
print("")
print("")
if opt=='1':
  import med
elif opt=='2':
  import sleep
elif opt=='3':
  import health
elif opt=='4':
  import water
else:
  print("this is not a valid option")
print("")
print("")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Thanks for using our project!")
print(" ") 
Cont=input("Press RETURN to close...")