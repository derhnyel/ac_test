import re
def word_frequency(sentences):
    wordcount_dict = {}
    for sentence in sentences:
        for word in sentence.split():
            if word in wordcount_dict:
                wordcount_dict[word]=wordcount_dict[word]+1
                continue 
            wordcount_dict[word] = 1
    wordcount_dict = sorted(wordcount_dict.items(),key =lambda x:x[1],reverse=True)        
    print("\n\n\n\n\n\n\n\\")
    print(wordcount_dict)              
    return wordcount_dict   
def check_query(value):
    if  value is not None:
        if value.isdigit():
            return True
    return False
        



    