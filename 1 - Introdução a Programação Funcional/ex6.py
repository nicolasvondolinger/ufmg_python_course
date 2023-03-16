def merge (L0, L1):
  if not L0:
    return L1
  if not L1:
    return L0
  else:
    H0 = head(L0)
    T0 = tail(L0)
    H1 = head(L1)
    T1 = tail(L1)
    if H0 < H1:
      return (H0, merge(T0, L1))
    else:
      return(H1, merge(L0, T1))