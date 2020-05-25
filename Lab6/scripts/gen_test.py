import random
import json

obj = {"gray cube": 0, "red cube": 1, "blue cube": 2, "green cube": 3, "brown cube": 4, "purple cube": 5, "cyan cube": 6, "yellow cube": 7, "gray sphere": 8, "red sphere": 9, "blue sphere": 10, "green sphere": 11, "brown sphere": 12, "purple sphere": 13, "cyan sphere": 14, "yellow sphere": 15, "gray cylinder": 16, "red cylinder": 17, "blue cylinder": 18, "green cylinder": 19, "brown cylinder": 20, "purple cylinder": 21, "cyan cylinder": 22, "yellow cylinder": 23}

ret = []
for i in range(32):
    r = random.sample(range(24), 3)
    ret.append([list(obj.keys())[x] for x in r])
print (json.dumps(ret))
