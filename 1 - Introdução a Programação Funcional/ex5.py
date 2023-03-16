def sorted(L):
  if not L:
    return True
  elif not tail(L):
    return True
  else:
    C1 = head(L) <= head(tail(L))
    return C1 and sorted(tail(L))
