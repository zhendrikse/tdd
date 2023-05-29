(def UNLOCKED 1)
(def LOCKING 2)
(def LOCKED 3)

; A locker wall is represented by a (hash)map.
; The keys are the locker numbers.
; The values are a tuple of locker state and the PIN code.
; This allows the locker to be in a state where it is waiting 
; for the PIN confirmation before it will be locked.
(def lockers {1 [UNLOCKED nil] 2 [UNLOCKED nil]})

(defn- locker-state [lockers, locker_id]
  (get (get lockers locker_id) 0))

(defn- locker-pin [lockers, locker_id]
  (get (get lockers locker_id) 1))

(defn- door-open? [locker_value]
  (or (= (get locker_value 0) UNLOCKED) (= (get locker_value 0) LOCKING)))

(defn- all-doors-open? [lockers]
  (map door-open? (vals lockers)))

(defn- locker-locking? [lockers locker_id]
  (= LOCKING (locker-state lockers locker_id)))

(defn- locker-locked? [lockers locker_id]
  (= LOCKED (locker-state lockers locker_id)))

(defn enter-pin [pin, locker_id, lockers]
  (if (locker-locked? lockers locker_id)
    (if (= pin (locker-pin lockers locker_id))
      (update lockers locker_id (constantly [UNLOCKED nil]))
      lockers)

    (if (locker-locking? lockers locker_id)
      (if (= pin (locker-pin lockers locker_id))
        (update lockers locker_id (constantly [LOCKED pin]))
        (update lockers locker_id (constantly [UNLOCKED nil])))
      (update lockers locker_id (constantly [LOCKING pin])))))

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

(run-tests)


