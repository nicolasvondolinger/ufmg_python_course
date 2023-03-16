def py2ll(list):
  if not list:
    return None
  else:
    return (list[0], py2ll(list[1:]))

