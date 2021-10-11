def create_dict(new_dict):  # Function that removes the special characters and creates the dictionary
    counter = 0  # counter for document numbers
    special_chars = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~.`: '  # All the special characters that interfere with search
    key_word = "<new document>"  # the word that separates the documents

    with open("ap_docs.txt", "r") as openfile:
        for line in openfile:
            line = line.lower()  # changes all the text to lowercase
            if key_word in line:
                counter += 1  # increase the counter/ document number if <new document> appears
            line = line.strip(special_chars)  # removes all the special characters
            line = line.split()  # splits the line into the words
            for word in line:
                if word not in new_dict:
                    create(new_dict, word, counter)  # put word in a dictionary
                elif word in new_dict:
                    create(new_dict, word, counter)  # put word in a dictionary
    return new_dict


def create(my_dict, key, value):  # function that turns the text files into a dictionary
    if key not in my_dict:
        my_dict[key] = list()  # creates a list for a word if it has not appeared before
    if value not in my_dict[key]:
        my_dict[key].append(value)  # puts the document number in the list if it is not there before
    return my_dict


def word_search(my_dict):  # Function to find the word/words in any document
    set1 = set()  # creates the sets
    set2 = set()
    my_str = input("enter:")

    if ' ' in my_str:  # check if two words were inputted
        word, word1 = my_str.split()
        for key, value in my_dict.items():
            if key == word.lower():
                set1 = value  # if the word matches the key it will put the doc number in the set
            if key == word1.lower():
                set2 = value  # if the word matches the key it will put the doc number in the set
        set3 = [value for value in set1 if value in set2]  # Cross references the two sets
        print("Documents fitting search:\n",
              set3)  # prints out only the numbers that appear in both sets
    elif ' ' not in my_str:  # if only one word was inputted
        for key, value in my_dict.items():
            if key == my_str:
                set1 = value  # if word matches the key it will put the doc number in the set
                print("Documents fitting search:\n",
                      set1)  # prints out the document number if only one word was inputted


def open_doc():  # Function to open the Documents
    try:
        my_file = open("ap_docs.txt", "r")
        number = int(input("Enter document number:"))  # asks the user for which document to open
        document = my_file.read()  # puts all the text into a variable
        document_list = document.split("<NEW DOCUMENT>")  # separates the documents by <NEW DOCUMENT>
        my_file.close()  # closes the file
        if len(document_list) > number > 0:
            print("Document #", number,
                  "\n-------------------------")
            print(document_list[number],
                  "\n-------------------------")  # returns the document that corresponds to the number
        else:
            print("Document #", number, "not found")
    except ValueError:
        print("No document found")


# End of functions


# Main body
while True:  # Main menu that will prompt the user
    dict1 = dict()  # creates the dictionary
    user_input = input("What would you like to do?\n"  # main interface
                       "1.Search for documents\n"
                       "2.Read Document\n"
                       "3.Quit Program\n"
                       ">")

    if user_input == '1':  # If user inputs 1
        create_dict(dict1)  # Function to create the dicitonary
        word_search(dict1)  # Function to find which document the word is in

    elif user_input == '2':  # If user inputs 2
        open_doc(),  # opens the text file

    elif user_input == '3':  # if user inputs 3
        quit()  # exits program

    else:  # if user inputs anything else
        print("Invalid input\n"  # error message 
              "-------------\n")
