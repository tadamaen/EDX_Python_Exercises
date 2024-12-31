# Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end
# of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you
# double-click on a file to open it, your computer uses its file extension to determine which program to launch.

# Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the
# web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the
# file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg.
# To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s
# media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is
# a common default.

# Step 1: Ask for an input file name
file_name = input("File name: ")

# Step 2: Conditional statements
if ".gif" in file_name:
    print("image/gif")
elif ".jpg" in file_name or ".jpeg" in file_name:
    print("image/jpeg")
elif ".png" in file_name:
    print("image/png")
elif ".pdf" in file_name or ".PDF" in file_name:
    print("application/pdf")
elif ".txt" in file_name:
    print("text/plain")
elif ".zip" in file_name:
    print("application/zip")
else:
    print("application/octet-stream")
