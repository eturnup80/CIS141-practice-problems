'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
file = open("gardening_tips.txt", "w")
file.write("Tip1: Lots of sun!\n")
file.write("Tip2: Plenty of water!\n")
file.write("Tip3: BEETHOVEN!\n")
file.close()


file  = open("gardening_tips.txt", "r")
content = file.read()
print(content[:18])
print(content[19:41])
print(content[42:])
file.close()

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    - Use a while loop to repeatedly ask for a hike name and distance in miles
    - Save each entry to hiking_log.txt (each hike on a new line)
    - When the user presses 0, exit the loop & print the contents of hiking_log.txt
'''
file = open("hikers_log.txt", "a")

while True:
    name = input("Please enter the name of the hiker. Enter 0 to exit. ")
    if name == "0":
        break
    distance = input("Please enter the number of miles that the hiker travelled. Enter 0 to exit.")
    if distance == "0":
        break
    file.write(name + "\t" + distance + "\n")
file.close()

with open("hikers_log.txt", "r") as file:
    print(file.read())
'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''

'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
yea_votes = 0
nay_votes = 0

with open("poll.txt", 'r') as file:
    for line in file:
        vote = line
        if vote == "yea":
            yea_votes += 1
        elif vote == "nay":
            nay_votes += 1

print(yea_votes)
print(nay_votes)
