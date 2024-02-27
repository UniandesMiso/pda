# Propiedades de los Alpes

## Estructura del proyecto

Este proyecto consta de dos microservicios y sigue una arquitectura hexagonal como se explica a continuación:

* src
 	* contracts: Esta carpeta contiene el microservicio de gestión contractual
		* api: Esta carpeta contiene la definición de los endpoints expuestos por el microservicio
		* config: Esta carpeta tiene la configuración del microservicio como ambiente de ejecución, URL de conexión a la base de datos, etc.
		* modules: Esta carpeta contiene los módulos del microservicio
			* sales: Esta carpeta contiene el módulo de ventas
				* application: Esta carpeta contiene la lógica del módulo (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
				* domain: Esta carpeta contiene la lógica del dominio del módulo, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
				* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
		* seedwork: Esta carpeta contiene componentes reutilizables y genéricos que pueden ser compartidos entre diferentes partes de la aplicación.
 	* properties: Esta carpeta contiene el microservicio de propiedades
		* api: Esta carpeta contiene la definición de los endpoints expuestos por el microservicio
		* config: Esta carpeta tiene la configuración del microservicio como ambiente de ejecución, URL de conexión a la base de datos, etc.
		* modules: Esta carpeta contiene los módulos del microservicio
			* sales: Esta carpeta contiene el módulo de ventas
				* application: Esta carpeta contiene la lógica del módulo (casos de uso) que implementa las reglas de negocio de la aplicación y coordina las interacciones entre los diferentes componentes.
				* domain: Esta carpeta contiene la lógica del dominio del módulo, incluyendo las entidades, objetos de valor, servicios del dominio, etc.
				* infrastructure: Esta carpeta contiene las implementaciones concretas de los componentes, externos, como repositorios a bases de datos.
		* seedwork: Esta carpeta contiene componentes reutilizables y genéricos que pueden ser compartidos entre diferentes partes de la aplicación.

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

## Escenario a probar

| Escenario de calidad: Procesamientos de transacciones de ventas históricas​ |
| --------------------------------------------------------------------------- |

| Escenario #: 4​         | Yo como sistema externo de información de transacciones inmobiliarias, cuando se procesan las transacciones de ventas históricas, dado que el modo de operación es normal, quiero que el módulo de gestión contractual pueda procesar diferentes formatos abiertos estandarizados correctamente el 100% de las veces.​ |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fuente​                 | Sistema de información de transacciones inmobiliarias​                                                                                                                                                                                                                                                                 |
| Estímulo​               | Envío de transacciones de ventas inmobiliarias históricas​                                                                                                                                                                                                                                                             |
| Ambiente​               | Operación normal​                                                                                                                                                                                                                                                                                                      |
| Artefacto​              | Módulo de gestión contractual​                                                                                                                                                                                                                                                                                         |
| Respuesta​              | Procesar correctamente todos las transacciones de ventas historicas​                                                                                                                                                                                                                                                   |
| Medida de la respuesta​ | 100% de transacciones procesadas exitosamente​                                                                                                                                                                                                                                                                         |
| Justificación​            | El uso de formatos abiertos estándar, mapeos y manejo de errores permite una integración con fuentes externas.​ |

| Decisiones Arquitecturales​           | Punto de sensibilidad​                   | Tradeoff​                                                             | Riesgo​                                                                                         |
| ------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| Mapeo y validación robusta​           | Correcto procesamiento de transacciones​ | Flexibilidad de diferentes formatos vs complejidad en la integración​ | Pérdida de datos críticos de transacciones inmobiliarias históricas al fallar su procesamiento​ |
| Manejo de errores personalizado​      | ​                                        | ​                                                                     | ​                                                                                               |
| Uso de formatos estándar (JSON, XML)​ | ​                                        | ​                                                                     | ​                                                                                               |
