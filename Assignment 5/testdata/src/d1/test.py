import timeit
import sys
import os

# import example


# print(sys.path)
# print(os.path)
# print(sys.executable)
# print(sys.version)
# # takes n + 1 steps


def sum1(n):
    final_sum = 0
    for x in range(n+1):
        final_sum += x
    return final_sum


print(sum1(10))


def sum2(n):
    return n*(n+1)/2


print(sum2(10))

setup1 = '''
def sum1(n):
  final_sum = 0
  for x in range(n+1):
      final_sum += x
  return final_sum
'''
stm1 = '''
sum1(10000)
'''


setup2 = '''
def sum2(n):
  return n*(n+1)/2
'''
stm2 = '''
sum2(10)
# '''

print(timeit.timeit(stm1, setup1, number=10000))
print(timeit.timeit(stm2, setup2, number=10000))
