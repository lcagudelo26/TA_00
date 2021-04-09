## Plan de Trabajo TA_00

El desarrollo de este proyecto se divide en varias etapas:

1. Diseño y aspectos técnicos.
2. Desarrollo:
   * 2.1 Frontend: Interfaz gráfica
   * 2.2 Backend: Funcionalidades de la aplicación
   * 2.3 Conexión base de datos

3. Validación y testing

### Listado de actividades requeridas para el desarrollo del proyecto:

**Diseño y aspectos técnicos**
* Determinar aspectos del diseño grafico para el prototipo de la aplicacion (gama de colores, estilo, tipografia, etc.)
* Diseño de las interfaces gráficas de la aplicación y el storyboard
* Determinar el lenguaje de programacion para la creacion de la aplicacion, el sistema operativo objetivo y el gestor de base de datos


**Desarrollo**

*Frontend*

* Implementar interfaz gráfica del inicio y registro de usuario (Correo, nombre usuario y contraseña.)
* Implementar interfaz gráfica del perfil
* Implementar interfaz gráfica de recomendaciones
* Implementar interfaz gráfica de opiniones/calificaciones



*Backend*

Acceso a funcionalidades básicas de la aplicación sin registro (público en general):
  * Acceso a la interfaz de recomendaciones por parte de un usuario sin registro, donde solo podrá buscarlas según la categoría y visualizarlas.
  * Acceso a la interfaz de opiniones/ calificaciones por parte de un usuario sin registro, donde solo podrá buscarlas según la categoría y visualizarlas.
  * Opción de registrarse en la aplicación o ingresar con una cuenta de usuario de google o facebook


Acceso a funcionalidades avanzadas de la aplicación con registro (usuarios registrados):
  * Acceso a la funcionalidad de realizar una recomendación (de acuerdo a una categoría en específico) por parte de un usuario con registro, donde podrá editarla y eliminarla una vez las haya publicado.
  * Acceso a la funcionalidad de realizar opiniones/ calificaciones (de acuerdo a una categoría en específico) por parte de un usuario con registro, donde podrá editarla y eliminarla una vez las haya publicado.
  * Funcionalidad de cerrar sesión
  * Funcionalidad de cambiar su contraseña
  * Funcionalidad de eliminar su cuenta
  * Funcionalidad de notificar problemas con la app en el centro de ayuda


Funcionalidades específicas según el tema del proyecto
  * Funcionalidad de agregar/eliminar en Mis favoritos cierta recomendación de acuerdo a su categoria.
  * Mostrar en la pantalla de inicio recomendaciones de mayor interes segun las preferencias del usuario y las calificiones recibidas
  * Notificaciones de las recomendaciones más gustadas en las categorias seleccionadas como favoritas por el usuario.
  * Mostrar resultados relacionados con una busqueda especifica en la parte de opiniones


**Conexión base de datos**

*Guardar información de usuarios:*
* Guardar información del registro de los usuarios: Correo, nombre usuario y contraseña.
* Guardar información de las publicaciones de recomendaciones y opiniones


**Validación y testing**
* Hacer validación de usuario de la aplicación
* Hacer el testing de la aplicacion 

************************************************************************


### A continuación se indican los contenidos que tendrán cada uno de los informes 03 a 10.

**Informe 03:** Diseño y aspectos técnicos
Fecha de entrega: 13 horas del viernes 16 de abril.

*Objetivo: el objetivo de este informe es desarrollar la parte grafica de la aplicacion,elegiremos el estilo que llevara la aplicacion, los colores adecuados, realizaremos bocetos manueles y posteriormente realizar digitalmente el storyboard,tambien estudiaremos lenguajes basicos de programacion que nos sean utiles para realizar nuestro proyecto.
Entregables:
* Determinar aspectos del diseño grafico para el prototipo de la aplicacion (gama de colores, estilo, tipografia, etc.)
* Diseño de las interfaces gráficas de la aplicación y el storyboard
* Determinar el lenguaje de programacion para la creacion de la aplicacion, el sistema operativo objetivo y el gestor de base de datos

**Informe 04:** Desarrollar la parte de programacion - *Frontend*
Fecha de entrega: 13 horas del viernes 23 de abril.

*Objetivo: el objetivo de esta entrega es desarrollar la parte mas basica de la programacion (frontend) para iniciar con la construccion de la aplicacion,construyendo las bases para el registro de los usuarios.

Entregables:
* Implementar interfaz gráfica del inicio y registro de usuario (Correo, nombre usuario y contraseña.)
* Implementar interfaz gráfica del perfil
* Implementar interfaz gráfica de recomendaciones
* Implementar interfaz gráfica de opiniones/calificaciones

**Informe 05:** Desarrollar la parte de programacion - Inicio Backend y Conexión base de datos
Fecha de entrega: 13 horas del viernes 30 de abril.

*Objetivo: el objetivo de esta entrega es continuar con los procesos de programacion pero esta vez enfocados en la conexion de la aplicacion con una base de datos para guardar la informacion de nuestros usuarios de forma segura,tambien implentremos funciones mas avanzadas para los usuarios que se registren el la aplicacion. 

Entregables:
* Realizar conexión con base de datos para guardar información del registro de los usuarios: Correo, nombre usuario y contraseña.
* Opción de registrarse en la aplicación o ingresar con una cuenta de usuario de google o facebook.
* Acceso a la funcionalidad de realizar una recomendación (de acuerdo a una categoría en específico) por parte de un usuario con registro, donde podrá editarla y eliminarla una vez las haya publicado.
* Acceso a la funcionalidad de realizar opiniones/ calificaciones (de acuerdo a una categoría en específico) por parte de un usuario con registro, donde podrá editarla y eliminarla una vez las haya publicado.

**Informe 06:** Desarrollar la parte de programacion - Continuación Backend y Conexión base de datos
Fecha de entrega: 13 horas del viernes 7 de mayo.

*Objetivo: el objetivo de este informe es conectar nuestra base de datos y comenzar a guardar informacion en ella, tambien realizar varias funciones mas espacificas de la aplicacion, como lo son las recomentaciones y calificaciones de diversos temas y generos.

Entregables: 
* Guardar información en base de datos de publicaciones de recomendaciones y opiniones
* Acceso a la interfaz de recomendaciones por parte de un usuario sin registro, donde solo podrá buscarlas según la categoría y visualizarlas.
* Acceso a la interfaz de opiniones/ calificaciones por parte de un usuario sin registro, donde solo podrá buscarlas según la categoría y visualizarlas.
* Funcionalidad de cerrar sesión
* Funcionalidad de cambiar su contraseña
* Funcionalidad de eliminar su cuenta
* Funcionalidad de notificar problemas con la app en el centro de ayuda


**Informe 07:** Desarrollar la parte de programacion - Finalización Backend 
Fecha de entrega: 13 horas del viernes 14 de mayo.

*Objetivo: es objetivo de este informe es crear un perfil del usuario basado en sus categorias favoritas,recomendaciones y preferencias para para que en su cuenta aparezcan sus temas de interes y hacer su experiencia mas agradable.

Entregables: 
* Funcionalidad de agregar/eliminar en Mis favoritos cierta recomendación de acuerdo a su categoria.
* Mostrar en la pantalla de inicio recomendaciones de mayor interes segun las preferencias del usuario y las calificiones recibidas
* Notificaciones de las recomendaciones más gustadas en las categorias seleccionadas como favoritas por el usuario.
* Mostrar resultados relacionados con una busqueda especifica en la parte de opiniones


**Informe 08:** Validación
Fecha de entrega: 13 horas del viernes 21 de mayo.

*Objetivo: el objetivo de esta entrega es hacer todas las pruebas necesarias para comprobar el correcto funcionamiento de la aplicacion, verificar que todo se encuentre en orden.

Entregables: 
* Hacer validación de usuario de la aplicación
* Establecer las mejoras a realizar de acuerdo a la validación de usuario
* Hacer el testing de la aplicacion 


**Informe 09:** Realiza cambios identificados en la validación
Fecha de entrega: 13 horas del viernes 28 de mayo.

*Objetivo: en esta entrega realizaremos los cambios que sean pertinentes y  necesarios  dependiendo de la validacion y el testing de la apliccacion para que nuestra aplicacion quede en excelentes condiciones.

Entregables: 
* Realizar cambios en la parte del Frontend y Backend identificados en la validación


**Informe 10:** Entrega final aplicación
Fecha de entrega: 13 horas del viernes 3 de junio.

*Objetivo: el objetivo de esta entrega es poder dar a conocer nuestra aplicacion al publico y hacer su respectiva exposicion.

Entregables: 
* Realizar cambios sugeridos en el informe 09





