


def perm(word: str): 
    if len(word) <= 2:
        return [word]
    
    cases = []
    for i in range(len(word)):
        fixed = word[i]
        rest = word[:i] + word[i+1:]

        for p in perm(rest):
            cases.append(p + fixed)

    return cases 



cache = {}
def dynamic_perm(word: str): 
    if len(word) <= 2:
        return [word]
    
    cases = []
    for i in range(len(word)):
        fixed = word[i]
        rest = word[:i] + word[i+1:]
         
        if rest in cache:
            perms = cache[rest]
        else: 
            perms = dynamic_perm(rest)
            cache[rest] = perms
        
        for p in perms: 
            cases.append(p + fixed)

    return cases 


import time 


start = time.perf_counter()
dynamic_perm("abcdefghijk")
print("exhaustive:", time.perf_counter() - start)

start = time.perf_counter()
perm("abcdefghijk")
print("dynamic:", time.perf_counter() - start)

