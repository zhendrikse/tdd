(defproject sudoku "0.0.1-SNAPSHOT"
  :description "Sudoku solver in Clojure"
  :plugins [[dev.weavejester/lein-cljfmt "0.11.2"]]
  :dependencies [[org.clojure/clojure "1.11.1"]]
  :target-path "target/%s"
  :profiles {:dev {:dependencies [[midje "1.6.0" :exclusions [org.clojure/clojure]]]
                   :plugins [[lein-midje "3.2.1"]]}}

  
