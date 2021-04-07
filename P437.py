# Problem Statement [Medium]
'''
Given a string and a set of charecters, return the shortest substring containing
all the charecters in the set.

Ex: string = 'figehaeci' and set = {a, e, i}
output : 'aeci'
'''

# TODO: Find and return the minimum length of substring from given string
# containing all the charecter in given subset
def find_min_substr(org_str, subset) -> str:
    s = set()
    curr_Char = ""
    nxt_idx = -1
    lst_substr = []
    substr = ""

    i=0 
    while i < len(org_str):
        for j in subset:
            found = False
            if org_str[i] == j and curr_Char == "" and len(s) < len(subset):
                substr = ""
                curr_Char = org_str[i]
                s.add(org_str[i])
                found = True
            elif org_str[i] == j and curr_Char != "" and len(s) < len(subset):
                s.add(org_str[i])
                nxt_idx = i if nxt_idx == -1 else nxt_idx
                found = True
            
            if len(s) == len(subset) and curr_Char != "":
                lst_substr.append(substr + org_str[i])
                curr_Char = ""
                i = nxt_idx - 1
                nxt_idx = -1
                s.clear()
                
            if found:
                break

        if curr_Char != "":
            substr += org_str[i]

        i += 1

    reslt = ""
    for i in lst_substr:
        if reslt == "":
            reslt = i
        elif len(i) < len(reslt):
            reslt = i

    return reslt

if __name__ == "__main__":
    org_str = 'abcdefabcf'
    subset = ['b', 'e', 'a']
    print(find_min_substr(org_str,subset))

    