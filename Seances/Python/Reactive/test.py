import rx
from rx import operators as ops
import sys
from rx import of
source = rx.from_iterable(sys.stdin)
#source = rx.from_iterable(open("./test.py"))
source.subscribe(
on_next = lambda i: print("Received {0}".format(i)),
on_error = lambda e: print("Error Occurred: {0}".format(e)),
on_completed = lambda: print("Done!"),
)
#d = rx.of(open("./test.py").read()).subscribe(on_next=print)
