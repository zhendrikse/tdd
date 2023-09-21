(defproject kata/game-of-life "0.1.0-SNAPSHOT"
  :description "Game of life in Clojure"
  :url "http://example.com/FIXME"
  :license {:name "EPL-2.0 OR GPL-2.0-or-later WITH Classpath-exception-2.0"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.10.0"]]
  :plugins [[dev.weavejester/lein-cljfmt "0.11.2"]]
  :main ^:skip-aot kata.game-of-life
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
