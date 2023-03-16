def mSort(L):
  if not L:
    return None
  if not tail(L):
    return L
  else:
    (L0, L1) = split(L)
    return  (mSort(L0), mSort(L1)) 