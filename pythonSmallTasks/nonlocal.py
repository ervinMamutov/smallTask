g_var = 0  # g_var in inner_test binds to a g_var top level
nl_var = 0
print('tp level -> g_var: {0} nl_var: {1}'.format(g_var, nl_var))


def test():
    nl_var = 2  # nl_var in inner_test binds to a nl_var in test
    print(('in test -> g_var: {0} nl_var: {1}'.format(g_var, nl_var)))

    def inner_test():
        global g_var  # g_var in inner_test binds to a g_var top level
        nonlocal nl_var  # nl_var in inner_test binds to a nl_var in test
        g_var = 1
        nl_var = 4
        print('in inner_test -> g_var: {0} nl_var: {1}'.format(g_var, nl_var))

    inner_test()
    print('in test -> g_var: {0} nl_var: {1}'.format(g_var, nl_var))


test()
print('top level -> g_var: {0} nl_var: {1}'.format(g_var, nl_var))
