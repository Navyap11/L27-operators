Amount= int(input("Please Enter Amount for Withdrawl : "))

note_1= Amount//100
note_2= (Amount%100)//50
note_3= ((Amount%100)%50)//10
note_4= ((Amount%100)%10)//1

print("Notes of 100 rupee: ", note_1)
print("Notes of 50 rupee: ", note_2)
print("Notes of 10 rupee: ", note_3)
print("Notes of 1 rupee: ", note_4)