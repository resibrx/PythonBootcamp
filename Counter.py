from collections import Counter

#quickly count the elements of a list
this_is_my_list = [1,1,2,2,3,4,5,6,1,9,2,8,8]
print(Counter(this_is_my_list))
s = 'skdoejrifuhjcioeifuheimjdiexdfcne'
print(Counter(s))

# count the words in a sentence
sentence = 'How many times does each word show up in this sentence word word shoe up up hello'
words = sentence.split()
print(Counter(words))

# Counter methods
c = Counter(words)
print(c.most_common(2))
print(sum(c.values()))
