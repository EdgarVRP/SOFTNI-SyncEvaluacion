with import <nixpkgs> {};

let
  pythonEnv = python37.withPackages (ps: with ps; [numpy pandas]);
in
  python37.mkDerivation {
    name = "SOFTNI-SyncEvaluacion";
    src = ./.;
    buildInputs = [ pythonEnv ];
    installPhase = ''
      mkdir -p $out
      cp -r ./* $out/
    '';
  }
