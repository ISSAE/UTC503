from functools import partial
import operator
from nums import is_prime

all_pred = lambda item, *tests: all(p(item) for p in tests)
any_pred = lambda item, *tests: any(p(item) for p in tests)

is_lt100 = partial(operator.ge, 100) # 100 > 
s_gt10 = partial(operator.le, 10) # 10 < 

all_pred(71, is_lt100, is_gt10)

predicates = (is_lt100, is_gt10)

all_pred(171, *predicates)
