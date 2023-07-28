(ns kata.locker-room
  (:gen-class))

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

(defn all-doors-open? [lockers]
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



