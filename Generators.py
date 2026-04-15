# GENERATOR EXAMPLES
# #wap to generate only the string with odd length
# in the
# #given list
# words=["king","queen","jack","kohli","hero"]
# def odd(words):
#     for i in words:
#         if len(i)%2!=0:
#             yield i
# g=odd(words)
# print(list(g))


# #wap to generate only the numeric value in list


# #wap to generate a list if it is individual data
# type
# #reverse it else keep it as it is
# #
a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"a":75}]
def gen(a):
    for i in a:
        if isinstance(i,(str)):
            yield i[::-1]
        else:
            yield i
g=gen(a)
print(list(g))



# #wap to return an iterator having the words and
# its length pair as a dictionary inside the tuple.
# # l=["charlie","golden
# retriever","scooby","sandy","german shepherd"]
#
# wap to generate a+b,a-b,a*b,a/b by taking a and b
# from user
# Prabhugouda
# wap to return a iterator which is having square
# root of values present in the list
# l=[25,36,49,81,9,16]
# wap to return a iterator having tuples of word
# and its len pair and typecast into dictionary
# l=["instagram","facebook","whatsapp","meta","orac
#  le"]
# wap to generate only numeric values in given list
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),4
#  5.36]
# wap to generate a list if it is individual data
# type reverse it else return as it is
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),4
#  5.36]
# wap to generate only the string with odd length
# in given list
# l=["alexa","siri","google","cortrena"]
# Prabhugouda
# wap to create a list of numbers if number are
# even square it else cube it
# l=[2,3,4,5,6,7]
# wap to return a list if words is of even length
# reverse it
# l=["hello","world","python","apple","google","wal
#  mart"]
# wap to generate the first letter of the word as
# key and words starting with letter as value
# s="python is a programming language and
# programming is part of life"
# output:-->[{'p': ['python', 'programming',
# 'programming', 'part'], 'i': ['is', 'is'], 'a':
# ['a', 'and'], 'l': ['language', 'life'], 'o':
# ['of']}]
# wap to generate a list if it is individual data
# type
# #reverse it else keep it as it is
# #
# a=["good",45,[1,2],78.6,(4,5),8+7j,{9,7},False,{"
#  a":75}]
# Prabhugouda
