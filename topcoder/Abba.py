"""https://arena.topcoder.com/index.html#/u/practiceCode/16527/48825/13918/2/326683"""


class Abba:

  def can_obtain(self, initial, target):
    startIdx = 0
    endIdx = len(target) - 1
    # direction can be +1 or -1. It's the sign of (startIdx - endIdx). You can
    # also picture it as the direction in which the endIdx is supposed to move
    # next along the X axis
    direction = -1
    initialLength = len(initial)
    targetLength = len(target)
    while targetLength >= initialLength:
      if (targetLength == initialLength
          and self.are_equal(initial, target, startIdx, direction)):
        return "Possible"

      removedCharacter = target[endIdx]
      endIdx += direction
      if removedCharacter == "B":
        # swap start and end indices
        tmp = startIdx
        startIdx = endIdx
        endIdx = tmp
        # reverse sign of direction
        direction = -direction
      targetLength -= 1

    return "Impossible"

  def are_equal(self, initial, target, startIdx, direction):
    length = len(initial)
    iTarget = startIdx
    iInitial = 0
    while length > 0:
      if initial[iInitial] != target[iTarget]:
        return False
      iInitial += 1
      # direction will be positive if startIdx falls after endIdx
      iTarget += -direction
      length -= 1
    return True
