(def data [[\A, \O, \T, \D, \L, \R, \O, \W],
        [\L, \C, \B, \M, \U, \M, \L, \U],
        ['D, \R, \U, \J, \D, \B, \L, \J],
        ['P, \A, \Z, \H, \Z, \Z, \E, \F],
        ['B, \C, \Z, \E, \L, \F, \H, \W],
        ['R, \K, \U, \L, \V, \P, \P, \G],
        ['A, \L, \B, \L, \P, \O, \P, \Q],
        ['B, \E, \M, \O, \P, \P, \J, \Y]])

(defn letter-column [letter-idx & {:keys [matrix] :or {matrix data}}]
(into [] (map #(nth % letter-idx) matrix)))

(defn above-or-below-letter [letter-idx & {:keys [above matrix] :or {above true matrix data}}]
(let [col (letter-column letter-idx matrix)]
    (if above (subvec col 0 letter-idx) (subvec col letter-idx))))

(defn word-matches [word letter-list]
(let [s (apply str letter-list)]
    (or (clojure.string/includes? s word)
        (clojure.string/includes? (clojure.string/reverse s) word))))

(defn check-surrounding-words [row letter-idx word]
(let [possible-words [(above-or-below-letter (- letter-idx 1))
                        (above-or-below-letter (- letter-idx 1) :above false)
                        (subvec row 0 letter-idx)
                        (subvec row (- letter-idx 1))]]
    (boolean (some #(word-matches word %) possible-words))))

(defn find-word [word & {:keys [matrix] :or {matrix data}}]
(let [first-letter (first word)
        matched-words (for [row matrix
                            [letter-idx letter] (map-indexed vector row)
                            :when (and (= first-letter letter) (check-surrounding-words row letter-idx word))]
                        1)]
    (reduce + matched-words)))

; ------------------
; U n i t  t e s t s
; ------------------
(use 'clojure.test)

(deftest find-word-hello
  (is (= 0 (find-word "HELLO"))))

(deftest fiind-word-world
  (is (= 0 (find-word "WORLD"))))

(deftest fiind-word-mbc
  (is (= 1 (find-word "MBC"))))

(deftest fiind-word-pop
  (is (= 3 (find-word "POP"))))

(run-tests)