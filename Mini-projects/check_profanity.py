import urllib

def read_text():
    document = open(r"D:\Programming\Python\Programming foundations with Python course\Lesson 5\check_profanity\text.txt")
    content = document.read()
    print('Lenght of file is: ' + str(len(content)))
    document.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    response = connection.read()
    connection.close()
    if 'true' in response:
        print("There's a curse word inside!")
    elif 'false' in response:
        print("Everythings fine!")
    else:
        print("Couldn't read a file")

read_text()
