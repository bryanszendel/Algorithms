#!/usr/bin/python

import argparse

def find_max_profit(prices):
  cache = []
  for i in range(len(prices)-1, 0, -1):
    outerInc = len(prices[0:i])
    innerInc = 1
    while outerInc > 0:
      top = prices[i]
      result = top - prices[i - innerInc]
      cache.append(result)
      innerInc += 1
      outerInc -= 1
  return max(cache)

print(find_max_profit([1050, 270, 1540, 3800, 2, 5000, 20000]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))