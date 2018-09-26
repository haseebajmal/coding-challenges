"""https://arena.topcoder.com/#/u/practiceCode/16320/46381/13645/2/325041

You are given two s: N and K. Lun the dog is interested in strings that satisfy
the following conditions:

  1. The string has exactly N characters, each of which is either 'A', 'B' or
   'C'.
  2. The string s has exactly K pairs (i, j) (0 <= i < j <= N-1) such that s[i] < s[j].

If there exists a string that satisfies the conditions, find and return any
such string. Otherwise, return an empty string.

- N will be between 3 and 30, inclusive.
- K will be between 0 and N(N-1)/2, inclusive.
"""


class Abc:

  def createString(self, n, k):
    for numAs, numBs, numCs in self.generateCounts(n):
      s = list("C" * numCs + "B" * numBs + "A" * numAs)
      if k == 0:
        return "".join(s)

      stopAt = 0 # or -1
      curK = 0
      moveCharAt = self.findFirstCharacterToMove(s, n)
      while moveCharAt != -1:
        if curK == k:
          # We achieved K
          return "".join(s)
        if moveCharAt == stopAt:
          stopAt += 1
          moveCharAt = self.findFirstCharacterToMove(s, n)
          continue
        # Move one to the left
        s[moveCharAt], s[moveCharAt - 1] = s[moveCharAt - 1], s[moveCharAt]
        moveCharAt -= 1
        curK += 1
    return ""

  def generateCounts(self, n):
    for numAs in range(0, n + 1):
      for numBs in range(0, n - numAs + 1):
          yield (numAs, numBs, n - numAs - numBs)

  def findFirstCharacterToMove(self, s, n):
    for i in range(n - 1, 0, -1):
      if s[i] < s[i - 1]:
        return i
    return -1
