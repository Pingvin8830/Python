import random

class Bone():
  def __init__(self, count_1, count_2):
    self.counts = [count_1, count_2]
    self.is_active = False
    random.shuffle(self.counts)

  def get_sum(self):
    return self.counts[0] + self.counts[1]

  def __str__(self):
    return 'Bone %d|%d' % (self.counts[0], self.counts[1])

class Deck():
  def __init__(self):
    self.bones = []
    for c1 in range(7):
      for c2 in range(c1, 7):
        self.bones.append(Bone(c1, c2))

  def shuffle(self):
    random.shuffle(self.bones)

