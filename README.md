# car_shop
Car Shopping website with CRUD funcionalities. Made with Django, Django RESTful API and some Javascript.

## Pasos para levantar el proyecto localmente

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_del_repositorio>

2. Instalar las dependencias:
pip install -r requirements.txt

3. Aplicar migraciones:
python manage.py migrate

4. Iniciar el servidor de desarrollo:
   python manage.py runserver

5. Acceder a la API:
Una vez que el servidor esté en funcionamiento, puedes acceder a la API en http://localhost:8000.

## Documentación de la API
La ruta /api/cars/ devuelve todos los coches.

Método HTTP: GET
Descripción: Esta ruta devuelve una lista de todos los coches en el sistema.
La ruta /api/cars/<id>/ devuelve los detalles de un coche específico.

Método HTTP: GET
Descripción: Esta ruta devuelve los detalles de un coche específico identificado por su ID.
Puedes crear un nuevo coche enviando una solicitud POST a /api/cars/.

Método HTTP: POST
Descripción: Esta ruta permite crear un nuevo coche en el sistema.
Puedes actualizar un coche existente enviando una solicitud PUT a /api/cars/<id>/.

Método HTTP: PUT
Descripción: Esta ruta permite actualizar los detalles de un coche existente identificado por su ID.
Puedes eliminar un coche existente enviando una solicitud DELETE a /api/cars/<id>/.

Método HTTP: DELETE
Descripción: Esta ruta permite eliminar un coche existente identificado por su ID.
La ruta /api/car_features/ devuelve todas las características de los coches.

Método HTTP: GET
Descripción: Esta ruta devuelve una lista de todas las características de los coches en el sistema.
Puedes actualizar una característica de un coche existente enviando una solicitud PUT a /api/car_features/<id>/update/.

Método HTTP: PUT
Descripción: Esta ruta permite actualizar una característica de un coche existente identificada por su ID.
Puedes eliminar una característica de un coche existente enviando una solicitud DELETE a /api/car_features/<id>/delete/.

Método HTTP: DELETE
Descripción: Esta ruta permite eliminar una característica de un coche existente identificada por su ID.
La ruta /api/car_info/ devuelve toda la información de los coches.

Método HTTP: GET
Descripción: Esta ruta devuelve una lista de toda la información de los coches en el sistema.
Puedes actualizar la información de un coche existente enviando una solicitud PUT a /api/car_info/<id>/update/.

Método HTTP: PUT
Descripción: Esta ruta permite actualizar la información de un coche existente identificada por su ID.
Puedes eliminar la información de un coche existente enviando una solicitud DELETE a /api/car_info/<id>/delete/.

Método HTTP: DELETE
Descripción: Esta ruta permite eliminar la información de un coche existente identificada por su ID.
