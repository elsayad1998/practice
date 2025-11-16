import matplotlib.pyplot as plt
import numpy as np
# Array Creation
arr = np . array ([1 , 2 , 3])
zeros = np . zeros ((2 , 3) )
ones = np . ones ((3 , 2) )
identity = np . eye (3)
# Array Operations
mean = np . mean ( arr )
std = np . std ( arr )
sum = np .sum ( arr )
print(f"sum = {sum}\n, std = {std}\n, mean = {mean}\n, identity = {identity.tolist()}\n, ones = {ones.tolist()}\n, arr = {arr.tolist()}\n, zeros = {zeros.tolist()}\n")




