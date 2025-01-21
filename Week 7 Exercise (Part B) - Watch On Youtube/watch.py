# It turns out that (most) YouTube videos can be embedded in other websites, just like the above.
# For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop, click Share, and then click
# Embed, you’ll see HTML (the language in which web pages are written) like the below, which you could then copy
# into your own website’s source code, wherein iframe is an HTML “element,” and src is one of several HTML “attributes”
# therein, the value of which, between quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.

# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player"
# frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
# allowfullscreen></iframe>

# Because some HTML attributes are optional, you could instead minimally embed just the below.

# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages
# (e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be URLs
# (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.

# In a file called watch.py, implement a function called parse that expects a str of HTML as input, extracts any
# YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter,
# shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below.
# Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no
# more than one such URL. If the input does not contain any such URL at all, return None.

#  http://youtube.com/embed/xvFZjo5PgG0
#  https://youtube.com/embed/xvFZjo5PgG0
#  https://www.youtube.com/embed/xvFZjo5PgG0

# Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see
# fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.


# Define the main function with the parse function
def main():
    print(parse(input("HTML: ")))


# Define the parse function
def parse(s):

    # From the HTML link, find the index of the string where src is (basically index of the letter s in src)
    src_start = s.find('src="')

    # If the HTML link does not contain any src
    if src_start == -1:
        return None

    # Shift the index of the start string such that it extracts the index of the letter h in http/https instead
    # Basically the index of h in http/https is 5 more than the index of s in src (simply add 5)
    else:
        src_start += 5

        # Obtain the end index of the src url by finding the next " after the h index
        src_end = s.find('"', src_start)

        # Use slicing the slice the url in the src (excluding the quote)
        src_value = s[src_start:src_end]

        # Filter out the irrelevant URLs - URLs with no youtube
        if "youtube" not in src_value:
            return None

        # Includes all the valid URLs (with youtube)
        else:
            # Split the url by the / character
            src_ls = src_value.split("/")

            # Extract the last element of the list, which is basically the random block of letters
            # (eg. xvFZjo5PgG0)
            url_code = src_ls[-1]

            # Return the string in the correct format
            return f"https://youtu.be/{url_code}"


if __name__ == "__main__":
    main()
