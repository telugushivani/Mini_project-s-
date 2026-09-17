name=input("enter student name: ")
maths=int(input("enter a maths marks:"))
telugu=int(input("enter a telugu marks:"))
english=int(input("enter a english marks:"))
hindi=int(input("enter a hindi marks:"))
science=int(input("enter a sciences marks:"))

total=maths+telugu+english+hindi+science
average=total/5
percentage=(total / 500) * 100

print("total:",total)
print("average:",average)
print("percentage:",percentage)
if percentage>=90:
  print("Grade A")
elif percentage>=80:
  print("Grade B")
elif percentage>=70:
  print("Grade C")
elif percentage>=60:
  print("Grade D")
elif percentage>=50:
  print("Grade E")
else:
  print("Grade F")