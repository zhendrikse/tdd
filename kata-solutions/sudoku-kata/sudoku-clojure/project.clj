(defproject sudoku "0.0.1-SNAPSHOT"
  :description "Sudoku solver in Clojure"
  :plugins [[dev.weavejester/lein-cljfmt "0.11.2"]]
  :dependencies [[org.clojure/clojure "1.11.1"]]
  :target-path "target/%s"
  :profiles {:dev {:dependencies [[midje "1.10.9"]]}
             ;; You can add dependencies that apply to `lein midje` below.
             ;; An example would be changing the logging destination for test runs.
             :midje {}})
             ;; Note that Midje itself is in the `dev` profile to support
             ;; running autotest in the repl.

  
