'''Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
Author: Savitri Sagar'''

def one_to_one_mapping(s1, s2):
    if len(s1) <= len(s2):
        d = {}
        for i in range(len(s1)):
            if s1[i] not in d:
                d[s1[i]] = s2[i]
                if d[s1[i]] != s2[i]:
                    return False
                return True
    return False


print(one_to_one_mapping("abc", "bcd"))