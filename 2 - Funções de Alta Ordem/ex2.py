make_inc_3 = lambda n: lambda x: x - n
inc = make_inc_3(1)
print(inc(3))