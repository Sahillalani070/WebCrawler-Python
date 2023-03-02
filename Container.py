"""
------------------------------------------------------------------------
[contain]
------------------------------------------------------------------------
File Name: Container.py
Version: 2021-07-29
------------------------------------------------------------------------
"""

# Import


# Constants

LETTER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

STOP_WORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 
'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 
'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
"she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 
'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 
'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
'about', 'against', 'between', 'into', 'through', 'during', 'before', 
'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 
'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 
'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 
'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 
'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 
'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', 
"couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 
'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', 
"mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 
'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', 
"won't", 'wouldn', "wouldn't"]
#the most common words gathered from a variety of dictionaries

# Functions

def Contain(file_name):
    """
    -------------------------------------------------------
    
    Use: word_list = Contain(file_name)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """
    file_handler = open(file_name, "r", encoding="utf8")
    
    word_list = extractText(file_handler)

    clean_list = useless(word_list)

    file_handler.close() # Close File handle

    return clean_list



def extractText(file_handler):
    """
    -------------------------------------------------------
    
    Use: words = extractText(file_handler)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    a = file_handler.read() # Reading File Content
    string = "" # Intializing String
    i = 0

    a = remove(a) # Remove Scripts from HTML File
    a = removecss(a)

    while i < len(a):
        # Skip HTML tags so that they are not concatenated to string
        if a[i] == '<':
            while a[i] != '>':
                i += 1
            
            i += 1

        # Only execute if it is an alphabet or space
        elif i < len(a)  and (a[i] in LETTER or a[i].isspace() == True):     
            string += a[i].lower() # Concatenate characters from string 'a' to string 'string'
            # print(a[i], end="") # Printing string (Testing only)
            i += 1
            
        # Move to next character
        else:
            i += 1

    string = removebin(string) # Removing Garbage and Punctuations

    word_list = string.split(" ") # Converting string to a Word List
    word_list = ' '.join(word_list).split() # Removing empty List Objects
    
    return word_list



def removebin(string):
    """
    -------------------------------------------------------
    
    Use: removebin(string)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """
    string = string.strip()

    # Removing all the symbols
    string = string.replace("`", "").replace("~", "").replace("!", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "")
    string = string.replace("^", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("-", "").replace("_", "")
    string = string.replace("+", "").replace("=", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "").replace(".", "")
    string = string.replace(";", "").replace(":", "").replace("|", "").replace("?", "").replace(",", "").replace("<", "").replace(">", "")
    string = string.replace("\n", " ")
    string = string.replace("\t", " ")

    return string



def remove(string):
    """
    -------------------------------------------------------
    Remove HTML Scripts from given string
    Use: string = remove(string)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    x = len(string) // 30

    # Loop till all script tags are removed
    for _ in range(x):
        if "<script" in string:
            starting_index = string.find("<script") 
            ending_index = string.find("</script>")
            string = string[:starting_index] + string[ending_index+9:]

    return string



def useless(word_list):
    """
    -------------------------------------------------------
    Remove Stop Words from given word_list
    Use: word_list = useless(word_list)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """
    new_list = []

    for i in word_list:
        if i not in STOP_WORDS:
            new_list.append(i) # Adding to new_list

    return new_list



def removecss(string):
    """
    -------------------------------------------------------
    Remove HTML Styles from given string
    Use: string = removecss(string)
    -------------------------------------------------------
    Parameters:
       x
    Returns:
       x
    ------------------------------------------------------
    """

    x = len(string) // 30

    for _ in range(x):
        if "<style" in string:
            starting_index = string.find("<style")
            ending_index = string.find("</style>")
            string = string[:starting_index] + string[ending_index+8:]

    return string