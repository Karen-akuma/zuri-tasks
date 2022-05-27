# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('story.txt', 'r') as f:
     file = f.read()

    f.close()

    return file
result = read_file_content('story.txt')
print(result)


def count_words():
    counts = dict()
    text = str.split()
    for t in text:
       if t in counts:
           counts[t] +=1
       else:
           counts[t] =1

    return counts
print(count_words(result))
