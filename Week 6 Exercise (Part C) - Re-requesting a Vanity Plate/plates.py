# From the main function, apply the is_valid function 
def main():
    input_name = input("Plate: ")
    boolean_value = is_valid(input_name)
    print(boolean_value)

# Obtained from https://github.com/mouhany/CS50P/tree/master/Week%205/test_plates as my intital
# function for the vanity plates exercise is not entirely correct

def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        if s[i].startswith("0") or s[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False

if __name__ == "__main__":
    main()

