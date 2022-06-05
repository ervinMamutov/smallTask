"""scopetest: text modul for visial area"""
v = 6
def f(x):
    """f: text function """
    print('global: ', list(globals().keys()))
    print('enter local: ', locals())
    y = x
    w = v
    print('exit local:', locals().keys())