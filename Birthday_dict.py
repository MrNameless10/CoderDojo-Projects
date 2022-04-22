import time
Birthdays ={
    "Albert Einstein": "14/3/1889",
    "Bill Gates": "28/10/1955",
    "Steve Jobs": "24/2/1955",
}
print("Welcome to the Birthday game ! We have the birthdays to:")
time.sleep(1)
for x in Birthdays:
    print(x)
    time.sleep(0.7)
choice= input("\nWho's birthday do you want to look up?")


other= input(print("who you want to add?"))
dia= input("dia")
Birthdays[other] = dia

print(Birthdays)

if choice in Birthdays:
    print("The birthday of {} is: ".format(choice))
    print(Birthdays[choice])

