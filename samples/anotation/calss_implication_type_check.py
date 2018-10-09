import sys
_annotated_classes = {}
debug_log = sys.stderr

def f1(arg):
    print("function f1")

    def callf(*args, **kwargs):
        debug_log.write('first argument: {}\n'.format(args[0]))
        rl = arg(*args, **kwargs)
        print(rl)
        return rl + " f1 return"

    return callf


@f1
def f2(arg=""):
    print("function f2")
    return arg + "f2 return"


def annotate(prototype):
    def ann(clz):
        _annotated_classes[clz] = prototype
        return clz
    return ann

@annotate(' bigint, bigint -> bigint ')
class Plus(object):
    def evaluate(self, a, b):
        if None in (a, b):
            return None
        return a + b


print("--func----")
print("--func----"+f2('sss'))

print("---class---")
p=Plus()
print("---class---"+p.evaluate(1,1))

