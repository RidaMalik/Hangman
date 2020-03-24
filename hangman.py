def g(correct):
	i=0
	wordlength=len(correct)
	guess="*"*wordlength
	guessed=[]
	for x in range(len(correct)):
		print("Enter the guess value")
		gl=input()
		if gl in guessed:
			print("The letter has been guessed")
			guessed.append(gl)
		if gl in correct:
			guessed.append(gl)
			print("Correct guess")
			for i in range(wordlength):
				if gl==correct[i]:
					guess=guess[:i]+correct[i]+guess[i+1:] 
			print(guess)
		else:
			print("Oops! Guessed letter not in the word")
			i=i+1
		if guess==correct:
			print("You have guessed the word!!")
			exit()
print("Welcome to the hangman game!!")
words=["apple","banana","cherry","guava","pineapple"]
import random
correct=random.choice(words)
print("Enter one to begin")
s=int(input())
if s==1:
	print(correct)
	print("*"*len(correct))
	g(correct)
else:
	print("Thank you")
	exit
