# Propiedades de los Alpes

## Despliegue

### Requisitos previos

Debes tener Docker Engine y Docker Compose en tu máquina. Para ello, puedes realizar cualquiera de las siguientes acciones:

* Instalar Docker Engine y Docker Compose como archivos binarios independientes.
* Instalar Docker Desktop, que incluye Docker Engine y Docker Compose.

> No necesitas instalar Python o PostgreSQL ya que estos son proporcionados por las imágenes de Docker.

### Instrucciones

1. Desde el directorio raiz de la aplicación inicia la aplicación ejecutando el siguiente comando:

	```
	docker compose up
	```

	Compose crea las imágenes necesarias para el código de la aplicación e inicia los servicios que se definieron. En este caso, el código se copia estáticamente en las imágenes en el momento de la compilación.
	
	Si quieres desplegar en modo detach (en segundo plano) utiliza:

	```
	docker compose up --detach
	```

2. Ya puedes empezar a utilizar los Servicios Web de la aplicación.

3. Para detener la aplicación y todos sus servicios, simplemente ejecuta el siguiente comando:

	```
	docker compose down
	```
