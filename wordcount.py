# def count_words(filename):
#     """ Iterates over each line in file, and prints word count of each word found
#     """

#     punctuation = ",.!?:;_\"\'"

#     word_count = {}
#     with open(filename) as file_of_words:

#         for line in file_of_words:
#             words = line.split()


#             for word in words:
#                 word = word.strip(punctuation)
#                 word = word.lower()
#                 word_count[word] = word_count.get(word, 0) + 1

#     for word, count in word_count.iteritems():
#         print word, count


# count_words("twain.txt")


# import sys

# print "HERES sys.argv"
# print sys.argv

# try:
#     filename = sys.argv[1]
# except IndexError:
#     raise Exception("Enter the file to open")
        


# punctuation = ",.!?:;_\"\'"

# word_count = {}
# with open(filename) as file_of_words:

#     for line in file_of_words:
#         words = line.split()


#         for word in words:
#             word = word.strip(punctuation)
#             word = word.lower()
#             word_count[word] = word_count.get(word, 0) + 1

# for word, count in word_count.iteritems():
#     print word, count



import collections
import sys

print "HERES sys.argv"
print sys.argv

try:
    filename = sys.argv[1]
except IndexError:
    raise Exception("Enter the file to open")
        


punctuation = ",.!?:;_\"\'"

all_words = []
with open(filename) as file_of_words:

    for line in file_of_words:
        words = line.split()
        all_words.extend(words)

        for word in words:
            word = word.strip(punctuation)
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.iteritems():
    print word, count

