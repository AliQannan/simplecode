print("hello in my computer")
name=input("Enter your name please ? : ")
eq=input(f"hello {name} ,if you went play type yes : ") 
x=eq.lower()
if x == "yes":
	print("welcom in the game ")
else:
	quit()
score=0
cpu=input("Enter your mean cpu ? ")
if cpu.lower() == "central processing unit":
	print("Correct")
	score+=1
else:
	print("Incorrect !")
ram=input("Enter your mean RAM : ")
if ram.lower() == "random access memory":
	print("Correct")
	score+=1
else:
	print("Incorrect")
	
print(f"your score you have {score} from 2 mark ! ")

