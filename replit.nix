{ pkgs }: {
  deps = [
    pkgs.vim
    pkgs.clojure
    pkgs.clojure-lsp
    pkgs.leiningen
    pkgs.graalvm17-ce
		pkgs.maven
		pkgs.replitPackages.jdt-language-server
		pkgs.replitPackages.java-debug
    pkgs.python39Full
    pkgs.replitPackages.prybar-python3
    pkgs.python39Packages.pip
    pkgs.python39Packages.poetry
    pkgs.python39Packages.pytest_6
    pkgs.python39Packages.pytest-watch
    pkgs.nodejs-14_x
		pkgs.nodePackages.typescript-language-server
		pkgs.yarn
		pkgs.replitPackages.jest
  ];
  PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
  LANG = "en_US.UTF-8";
}