#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  cache = {0:1, 1:1, 2:2}
  def cache_inner(n):
    nonlocal cache
    if n not in cache:
      cache[n] = cache_inner(n-1) + cache_inner(n-2) + cache_inner(n-3)
    return cache[n]
  return cache_inner(n)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')