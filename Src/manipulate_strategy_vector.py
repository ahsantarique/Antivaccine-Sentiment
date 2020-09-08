'''manipulate strategy vector'''

def make_antivax(strategy, s):
  for i in s:
    strategy[i] = 1
  return strategy


def make_provax(strategy, s):
  for i in s:
    strategy[i] = 0

  return strategy

def is_subset(lst1, lst2):

  for i in lst1:
    if( i not in lst2):
      # print(i)
      return False

  return True

def get_antivax(strategyNE):
  s = []
  for i in strategyNE.keys():
    if (strategyNE[i] == 1):
      # print(i)
      s.append(i)
  
  return s