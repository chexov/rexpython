=========
RexPython
=========

This is python Rx implementation mimicing RxJava API as far as it can.


Installation
============
pip install rexpython

=====
Usage
=====
import rexpython as rx

frames = rx.Observable.create(lambda emitter: on_subscribe(emitter, video_url, 2))
mat_img = frames.map(featureextractor.FeatureExtractor.preprocess_image)
vect = mat_img.map(lambda img: fe.get_activations([img]))
words = vect.map(lambda vec: d.getWordsForBatch(vec, 40)) \
    .flatMap(lambda wlist: rx.Observable.from_(wlist))
words = words.doOnNext(lambda w: log.info("words=%s" % w)).doOnError(lambda err: log.error("ERRRORRR %s" % err))
value = words.toList().blockingGet()
