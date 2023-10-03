{ pkgs }: {
  deps = [
    pkgs.stdenv.cc.cc.lib
    #pkgs.zlib
    #pkgs.glib
    #pkgs.xorg.libX11
    #pkgs.glibc
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
    pkgs.cookiecutter
    pkgs.pipreqs
    pkgs.python311Full
    pkgs.python311.pkgs.pip
    pkgs.python311.pkgs.pytest-watch
    pkgs.python311.pkgs.pytest
    pkgs.python311.pkgs.virtualenv
    pkgs.poetry
    pkgs.nodejs-18_x
		pkgs.nodePackages.typescript-language-server
		pkgs.yarn
    pkgs.esbuild
    pkgs.nodePackages.typescript
  ];
  # environment = {
  #   sessionVariables = {
  #     LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
  #   };
  # };
  # PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
  #     pkgs.stdenv.cc.cc.lib
  #     pkgs.zlib
  #     pkgs.glib
  #     pkgs.xorg.libX11
  # ];
  #PYTHON_LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}";
  PYTHONHOME = "${pkgs.python311}";
  PYTHONBIN = "${pkgs.python311}/bin/python3.11";
  LANG = "en_US.UTF-8";
}
