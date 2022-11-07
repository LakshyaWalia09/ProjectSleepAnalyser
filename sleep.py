#--------------------------------#
# Beginning

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("Welcome to Sleep Score Aanalyser!")
print("")
print("")
print("Press RETURN to continue.")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("")
print("")
print("")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#Sleep data, saved inside LIST sequence.
print("We need some information in order to get your sleep data")
print("")
print("NOTE: We store data in list sequence so this instruction is important else program may crash!")
print("")
print("Please provide data in this format only: ")
print("               [HOUR,MINUTE]")
sleepdata=eval(input("Sleep time: "))
sleephr,sleepmin=0,0
sleephr,sleepmin=sleepdata

#Wake data, saved inside LIST sequence.
wakedata=eval(input("Wake time: "))
wakehr,wakemin=0,0
wakehr,wakemin=wakedata

#------------------------#
#Main calculations are done here.

#Time slept before midnight
timemid=11-sleephr
timemin=(1-(sleepmin/60))
timemid=timemin+timemid

#Sleep time totalling:
timeslept_total=timemid+wakehr+(wakemin/60)

#Total time formatting:
hrslept=int(timeslept_total)
minslept=int((timeslept_total%1)*60)

#this conditional here basically chooses from either just showing hours or also minutes because why not
print("Total time slept: ",hrslept,"hrs and",minslept,"mins")