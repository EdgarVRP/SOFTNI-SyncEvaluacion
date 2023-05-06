{ pkgs ? import <nixpkgs> {} }:
pkgs.python37Packages.buildPythonApplication {
  pname = "SOFTNI-SyncEvaluacion";
  src = ./.;
  buildInputs = [ pkgs.python37Packages.flask ];
}
