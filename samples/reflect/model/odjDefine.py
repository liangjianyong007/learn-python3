class A(object):
    def print_name(self):
        print('this is A')

class B(A):
    def print_name(self):
        print('this is B')


class C(A):
    def print_name(self):
        print('this is C')