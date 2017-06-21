import sys
import time
from unittest import TestCase

from rexpython import Observable, LambdaObserver, ActionDisposable, Disposable


class TestObservable(TestCase):
    def test_blockingSubscribe(self):
        d = Observable.from_(xrange(1, 4)).blockingSubscribe(
            on_next=lambda i: sys.stdout.write("from=%s\n" % i),
            on_complete=lambda: sys.stdout.write("!! complete\n")
        )

        print d
