{ pkgs }: {
  deps = [
		pkgs.nettools
  pkgs.jq.bin
    pkgs.dotnet-sdk_7
    pkgs.omnisharp-roslyn
    pkgs.gradle_7
    pkgs.nodePackages.prettier
    pkgs.vim
    pkgs.clojure
    pkgs.clojure-lsp
    pkgs.leiningen
    pkgs.graalvm17-ce
		pkgs.maven
    pkgs.pipenv
    pkgs.poetry
    pkgs.cookiecutter
    pkgs.pipreqs
    pkgs.python310Full
    pkgs.python310Packages.pip
    pkgs.python310Packages.pytest_6
    pkgs.python310Packages.pytest-watch
    pkgs.nodejs-18_x
		pkgs.yarn
    pkgs.esbuild
    pkgs.nodePackages.typescript
    pkgs.nodePackages.typescript-language-server
  ];
  PYTHONHOME = "${pkgs.python310Full}";
  PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
  LANG = "en_US.UTF-8";
  STDERREDBIN = "${pkgs.replitPackages.stderred}/bin/stderred";
  PRYBAR_PYTHON_BIN = "${pkgs.replitPackages.prybar-python310}/bin/prybar-python310";
}
