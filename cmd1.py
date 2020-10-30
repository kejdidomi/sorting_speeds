import sys
import random
import time
import sys
v = random.sample(range(100000000), int(sys.argv[1]))
a = time.time()
v.sort()
b = time.time()
print("{}".format((b-a)))
