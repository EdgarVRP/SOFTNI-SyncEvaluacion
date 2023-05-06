# SOFTNI_SyncEvaluacion

Instrucciones:

pip install Flask

pip install Flask-RESTful

pip install pymongo

pip install python-dotenv

para correr el servicio flask run

Se instala flask-cors para permitir solicitudes agenas al servidor backend

pip install flask-cors

Se instala el paquete python-dotenv para manejar las variables de entorno

pip install python-dotenv

Para el despliegue en railway es necesario:

crear el archivo default.nix

```
{ pkgs ? import <nixpkgs> {} }:
pkgs.python37Packages.buildPythonApplication {
  pname = "my-flask-app";
  src = ./.;
  buildInputs = [ pkgs.python37Packages.flask ];
}
```

Se crea el archivo `Procfile` en la raiz con lo siguiente:

`web: nix-shell --run "python app.py" --pure`
