# given 2 strings ransomNote and magazine -> True is ransoMNote can be constructed from magazine, else False

def ransomnote(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    hash_1 = {}
    hash_2 = {}
    for i in range(len(ransomNote)):
        hash_1[ransomNote[i]] = 1 + hash_1.get(ransomNote[i],0)
    for j in range(len(magazine)):
        hash_2[magazine[j]] = 1 + hash_2.get(magazine[j],0)
    for i, value in hash_1.items():
        if i not in hash_2 or value > hash_2[i]:
            return False
    return True

# O(n) time and O(1) space actually since hash map is bound by 26 lowercase letters, so space is constant.