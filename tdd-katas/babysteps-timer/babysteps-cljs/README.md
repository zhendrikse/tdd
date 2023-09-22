# Babysteps timer in Clojure script

## Development

To get an interactive development environment run:

    lein fig:build

This will auto compile and send all changes to the browser without the
need to reload. After the compilation process is complete, you will
get a Browser Connected REPL. An easy way to try it is:

    (js/alert "Am I connected?")

and you should see an alert in the browser window.

To clean all compiled files:

	lein clean

To create a production build run:

	lein clean
	lein fig:min

## VS code with Calva

The project is created using

```bash
$ lein new figwheel-main hello-world.core -- +npm-bundle --reagent
```

 1. Run `npm install` to install the npm modules and then open the project in VS Code.
 2. From the command palette, choose Jack-in
 3. Choose ”Leiningen + Figwheel Main” project type
 4. Choose ”No alias”
 5. Choose ”dev” profile
 6. Wait for Clojure REPL to start
 7. Choose to start ”dev” build
 8. Wait for ClojureScript REPL to start, which then opens the ClojureScript app in the web browser
 9. Choose to connect to the ”dev” build
10. Open the `src/figwheel_main_from_lein_template/core.cljs` and Load Current File and dependencies
11. Hack away.

