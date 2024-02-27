# Propiedades de los Alpes

## Estructura del proyecto

Este proyecto consta de dos microservicios y sigue una arquitectura hexagonal como se explica a continuación:

* src
 	* contracts: Esta carpeta contiene el microservicio de gestión contractual
  		* application: Esta carpeta contiene la lógica de aplicación (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
  		* domain: Esta carpeta contiene la lógica del dominio de la aplicación, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
  		* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
 	* properties: Estra carpeta contiene el microservicio de gestión de propiedades
  		* application: Esta carpeta contiene la lógica de aplicación (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
  		* domain: Esta carpeta contiene la lógica del dominio de la aplicación, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
  		* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.

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
