def inarray(value, other):
    if value is None: return False
    for v in set(value):
        if v == 'all': return True
        if v in set(other): return True
    return False


class TestModule(object):

    def tests(self):
        return {
            'inarray': inarray,
        }