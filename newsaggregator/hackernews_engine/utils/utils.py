import re
def word_frequency(sentences):
    wordcount_dict = {}
    reg = re.compile(r'\w+')
    for sentence in sentences:
        for word in sentence.split():
            word_regex_length = len(reg.findall(word))
            if word_regex_length == 1:
                if word in wordcount_dict:
                    wordcount_dict[word]=wordcount_dict[word]+1
                    continue 
                wordcount_dict[word] = 1    
    wordcount_dict = sorted(wordcount_dict.items(),key =lambda x:x[1],reverse=True)                    
    return wordcount_dict   
def check_query(value):
    if  value is not None:
        if value.isdigit():
            return True
    return False
        



    