# Some people have a habit of speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed,
# or even by having them pause between words.

# In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

# Step 1: Ask the user for his/her input
name = input("What do you want to say? ")

# Step 2: State the input, replacing each space with ...

# Step 2.1: Create a new list ls
ls = []
combined_string = ""

# Step 2.2: Split the string into individual words
split_words = name.split(" ")

# Step 2.3: Iterate over the list of split_words and add the ... to all words except for the last
for i in range(0,len(split_words) - 1):
    final_result = split_words[i] + '...'
    ls.append(final_result)

# Step 2.4: Don't forget to add in the last word of the list that is not involved in the for loop
ls.append(split_words[-1])

# Step 2.5: Iterate over the new ls and concatenate all the individual words into one with the ... inserted
for j in range(0, len(ls)):
    combined_string = combined_string + ls[j]

# Print the resulting combined string
print(combined_string)
