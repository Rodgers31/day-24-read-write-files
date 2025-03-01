with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()

# you have to change mode write w= add a= add text on top of existing
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# will automatically create a file if it doesn't exist
with open("testing.txt", mode="w") as file:
    file.write("\n Bobby")