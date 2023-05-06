{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python37.withPackages (ps: with ps; [numpy pandas]);
in
  pkgs.python37.mkDerivation {
    name = "SOFTNI-SyncEvaluacion";
    src = ./.;
    buildInputs = [ pythonEnv ];
    installPhase = ''
      mkdir -p $out
      cp -r ./* $out/
    '';
  }
