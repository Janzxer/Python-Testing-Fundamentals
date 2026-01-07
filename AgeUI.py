import AgeUtils

age = 0

while age != "exit":
    age = input("Tell me your age. Type 'exit' to quit. ")

    if age == "exit":
        print("Farewell")
    else:
        print(AgeUtils.AgeVerification(age))

# JANNE VILJANEN TKM24