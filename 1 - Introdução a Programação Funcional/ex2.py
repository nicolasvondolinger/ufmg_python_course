def ll2py(list):
  if not list:
    return []
  else:
    h = head(list)
    t = tail(list)
    return [h] + ll2py(t)