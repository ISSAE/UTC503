class Y:
      def f(x):
            raise AssertionError("pas encore définie")
      def g(x):
            return "Y"
  
class X(Y):
    def __m(self):
        return ('dans __m')
    def f1(self):
      return(self.__m())


'''$ python -i encapsul.py 
>>> x=X()
>>> dir(x)
['_X__m', '__doc__', '__module__']
>>> x.m()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: X instance has no attribute 'm'
>>> x.__m()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: X instance has no attribute '__m'
>>> x._X__m()
'dans __m'
>>> '''