(ns kata.locker-room-test
  (:require [clojure.test :refer :all]
            [kata.locker-room :refer :all]))

; ------------------
; U n i t  t e s t s
; ------------------
(use 'clojure.test)

(deftest initially-all-lockers-are-unlocked
  (is (= `(true true) (all-doors-open? lockers))))

(deftest a-PIN-on-an-open-locker-prepares-to-lock-it
  (let [pin-entered-once-on-locker-1 (enter-pin "1234" 1 lockers)]
    (is (= `(true true) (all-doors-open? pin-entered-once-on-locker-1)))))

(deftest same-PIN-twice-on-an-open-locker-actually-locks-it
  (let [pin-entered-twice-on-locker-1 (enter-pin "1234" 1 (enter-pin "1234" 1 lockers))]
    (is (= `(false true) (all-doors-open? pin-entered-twice-on-locker-1)))))

(deftest two-different-PINs-on-an-open-locker-keep-it-unlocked
  (let [pin-entered-once-on-locker-1 (enter-pin "1234" 1 lockers)]
    (is (= `(true true) (all-doors-open? (enter-pin "4321" 1 pin-entered-once-on-locker-1))))))

(deftest correct-PIN-on-a-locked-locker-unlocks-it
  (let [pin-entered-twice-on-locker-1 (enter-pin "1234" 1 (enter-pin "1234" 1 lockers))]
    (is (= `(true true) (all-doors-open? (enter-pin "1234" 1 pin-entered-twice-on-locker-1))))))

(deftest wrong-PIN-on-a-locked-locker-keeps-it-locked
  (let [pin-entered-twice-on-locker-1 (enter-pin "1234" 1 (enter-pin "1234" 1 lockers))]
    (is (= `(false true) (all-doors-open? (enter-pin "4321" 1 pin-entered-twice-on-locker-1)))))) 
