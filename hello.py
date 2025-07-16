name = input("Enter your name: ")
print(f"Hi, {name}!")

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

print("Counting to 5:")
for i in range(1, 6):
    print(i)
