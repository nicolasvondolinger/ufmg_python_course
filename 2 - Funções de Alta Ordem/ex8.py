def appendL(L1, L2):
  if not L1:
    return L2
  elif not L2:
    return L1
  else:
    return (head(L1), appendL(tail(L1), L2))