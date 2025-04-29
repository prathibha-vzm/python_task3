import random
#Question 1:
print("The USer has to guess the number that might come next.")

while True:
    try:
        print("Enter values between 1-7")
        in_user = int(input())
        rand= random.randint(1,7)

    except ValueError:
        print("Enter Valid Number")
        continue
    print(rand)
    if in_user == rand:
         print("Correct")
         break
    elif in_user < rand:
         print("Too Low")
         continue
    else:
         print("Too High")
         continue

#Question 2:
print("\nA list of words are scrambled and guess the correct word")


words = ["python", 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

rand=random.choice(words)
rand_list = list(rand)

random.shuffle(rand_list)
join_rand=''.join(rand_list)

print("Guess the word",join_rand)


while True:
    try:
        print("Enter your Answer")
        user_input = input()
    except ValueError:
        print("Enter Valid Answer")
        continue
    if user_input==rand:
        print("Correct")
        break
    else:
        print("Try again")
        continue        

