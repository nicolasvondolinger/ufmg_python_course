def incN(L, N):
  return mapL(L, lambda x: x + N)

test("map-inc-N", incN((1, (2, None)), 2), (3, (4, None)))