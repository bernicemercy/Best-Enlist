
                #DAY 2 ----- STRING

#how to print a value 
print("30 days 30 hour challenge")
print('30 days 30 hour challenge')

# Assigning value to variable

Hours = "thirty"
print(Hours)

#indexing using string

Days = "thirty days"
print(Days[0])

#print particular character from certain text

Challenge = "I will win"
print(Challenge[7:10])

#length of Character

print(len(Challenge))

#Convert String into lower character

print(Challenge.lower())

#Concatention

a = "30 Days"
b = "30 hours"
c = a+b
print(c)

#Adding space during concatenation

print(a+" "+b)

#casefold() - usage
text = "Thirty days thirty hour challenge"
x = text.casefold()
print(x)
print(text.capitalize())
print(text.find("days"))
print(text.isalpha()) #returns false as the statement has space
print(text.isalnum())
