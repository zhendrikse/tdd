{ pkgs }: {
  deps = [
    pkgs.vimHugeX
    #pkgs.python310Full
    #pkgs.replitPackages.prybar-python310
    #pkgs.replitPackages.stderred
    #pkgs.python310Packages.pip
    #pkgs.python310Packages.pytest_6
    #pkgs.python310Packages.pytest-watch
    #pkgs.poetry
    pkgs.jq.bin
    pkgs.dotnet-sdk_7
    pkgs.stdenv.cc.cc.lib
    pkgs.gradle_7
    pkgs.nodePackages.prettier
    pkgs.vim
    pkgs.clojure
    pkgs.clojure-lsp
    pkgs.leiningen
    pkgs.graalvm17-ce
    pkgs.maven
    #pkgs.replitPackages.jdt-language-server
    #pkgs.replitPackages.java-debug
    #pkgs.pipenv
    pkgs.cookiecutter
    #pkgs.pipreqs
    #pkgs.nodejs-20_x
    pkgs.yarn
    #pkgs.replitPackages.jest
    pkgs.esbuild
    pkgs.nodePackages.typescript
    #pkgs.nodePackages.typescript-language-server
  ];
  PYTHONHOME = "${pkgs.python310Full}";
  PYTHONBIN = "${pkgs.python310Full}/bin/python3.10";
  LANG = "en_US.UTF-8";
  #STDERREDBIN = "${pkgs.replitPackages.stderred}/bin/stderred";
  #PRYBAR_PYTHON_BIN = "${pkgs.replitPackages.prybar-python310}/bin/prybar-python310";
  LD_LIBRARY_PATH= "${pkgs.stdenv.cc.cc.lib}/lib/";
}