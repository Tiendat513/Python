from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

result = "DIFFERENT"
s1 = input().strip()
s2 = input().strip()

if s1 == "END" and s2 == "END":
    pass
elif are_anagrams(s1, s2):
    result = "SAME"

print(result)