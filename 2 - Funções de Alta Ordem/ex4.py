"My Code"

"""def filterOdds(L):
  if not L:
    return None
  elif not tail(L):
    if head(L) % 2 != 0:
      return head(L)
    else:
      return None
  else:
    if head(L) % 2 != 0:
      return (head(L), filterOdds(tail(L)))
    else:
      return (filterOdds(tail(L)))"""

"/////////////////////////////////////////////"

"Fernando's Code"

def filterOdds(L):
  return filterL(L, lambda x: x % 2)
  
