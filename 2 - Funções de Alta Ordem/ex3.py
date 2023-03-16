def filterL(L, f):
  if not L:
    return None
  else:
    T = filterL(tail(L), f)
    H = head(L)
    if f(H):
      return (H, T)
    else:
      return T