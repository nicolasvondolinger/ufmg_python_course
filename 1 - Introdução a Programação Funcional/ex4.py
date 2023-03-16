def split (L):
  if not L:
    return (None, None)
  if not tail(L):
    return(L, None)
  else:
    h0 = head(L)
    h1 = head(tail(L))
    (t0, t1) = split(tait(tail(L)))
    return ((h0, t0), (h1, t1))