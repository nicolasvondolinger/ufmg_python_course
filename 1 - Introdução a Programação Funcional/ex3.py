def size(list):
  if not list:
    return 0
  else:
    return 1 + size(tail(list))