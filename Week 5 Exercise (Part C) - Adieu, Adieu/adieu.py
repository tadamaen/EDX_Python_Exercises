# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user
# inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names,
# separating two names with one and, three names with two commas and one and, and names with commas and one and

name_list = []
string = "Adieu, adieu, to "
final_string = ""

while True:
    try:
        name = input("Name: ")
        name_list.append(name)
    except EOFError:
        print("\n")
        if len(name_list) > 2:
            final_string = string + ", ".join(name_list[:-1]) + ", and " + name_list[-1]
        elif len(name_list) == 2:
            final_string = string + ", ".join(name_list[:-1]) + " and " + name_list[-1]
        elif name_list:
            final_string = string + name_list[0]

        print(final_string)
        break

