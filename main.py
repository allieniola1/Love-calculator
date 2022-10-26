# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_names = name1 + name2
case_check = both_names.lower()

t = case_check.count('t')
r = case_check.count('r')
u = case_check.count('u')
e = case_check.count('e')

true = t + r + u + e

l = case_check.count('l')
o = case_check.count('o')
v = case_check.count('v')
e = case_check.count('e')

love = l + o + v + e
love_score = str(true) + str(love)
int_score = int(love_score)

if (int_score < 10) or (int_score > 90):
  print(f"Your score is {int_score}, you go together like coke and mentos.")

elif (int_score >= 40) and (int_score <= 50):
  print(f"Your score is {int_score}, you are alright together.")

else:
  print(f"Your score is {int_score}.")


