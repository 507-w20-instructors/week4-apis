
def this_func(this_param=[1, 2, 3]):
    t = this_param.copy()
    print(t)
    t.append(4)

this_func()
this_func()