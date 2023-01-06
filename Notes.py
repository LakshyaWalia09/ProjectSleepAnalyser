# Notes of sleep

20 line's snippet:

#Sleep data is converted from string to useful info in simple steps:
# 1) input data from user aand save as string
# 2) now we split that time into list and remove ':' element from list as its not required
# 3) now we save time of hour and minutes in two different variables and simply convert into integers 

20 line's snippet:

#Different from normal algebra due to data being time.
# 1) First we subtract time before sleep from 11 (not 12 as 1 hour is take as minutes and used to calculate sleep minutes.)
# 2) then we devide sleep minutes from 60 to make it hours and then subtract it from 1
# 3) now we add them both making a total time slept before midnight (saved in timemid variable)
# 4) Now we calculate the total sleep time for this we add timemid and wake hr and wakemin (wakemin also converted into hours) 
# 5) Now we convert the sleeptime into integer so that any minutes (which will be after decimal places) gets excluded and we have the sleep hours and 
# 6) And for sleep minutes we take the total time and remainder it from 1 making the number only have the decimal (minutes) value and multiply with 60 to convert it into minutes format

#cancelled
#Loading screen (Supposed to have a short time period beween each element being shown but doesnt seem to work.)
a=''
for i in range(25):
	if i==0:
		a='Analysing Data... '
	elif i==1:
		a='['
	elif i==23:
		a='] '
	elif i==24:
		a='100%'
	else:
		a='='
	print(end=a)
print()
a=''
for i in range(25):
	if i==0:
		a='Creating Report... '
	elif i==1:
		a='['
	elif i==23:
		a='] '
	elif i==24:
		a='100%'
	else:
		a='='
	print(end=a)
	
#CANCELLED
#Health ke liye coding ka idea:


I think user se pehele age and name input 

then info (feeling wagera wagera) as a string lenge user se 

fir us sabko list mein convert kardenge

then loop chala denge for loop
jo check karega har element 

ham aise 5 variables rakh sakte hain like
cough, temperature, body pain, headache, restlessness
ek add kardenge unke variables mein ki ye wala symptom hai user mein

then uske bad jo main deseases rehete hain unko if satetements mein rakh denege (a5 hi karte i think sufficient hai)

example
if cough!=0 and headache!=0 
print()
fir suggestions wagera print kardenge