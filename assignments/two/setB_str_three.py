def count(s1, s2):
    c=0
    j=0
    for i in s1:
        if s2.find(i)>-0 and j==s1.find(i):
            c=c+1
        j=j+1
    print("Matching char: ",c)

s1="aabcdefk12"
s2="b2acdefk1"
count(s1,s2)