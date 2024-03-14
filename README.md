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
Una vez que el servidor esté en funcionamiento, puedes acceder a la API en http://127.0.0.1:8000/

## Documentación de la API
La ruta /api/cars/ devuelve todos los coches.<br>
Método HTTP: GET<br>
Descripción: Esta ruta devuelve una lista de todos los coches en el sistema.<br>

La ruta /api/cars/"id"/ devuelve los detalles de un coche específico.<br>
Método HTTP: GET<br>
Descripción: Esta ruta devuelve los detalles de un coche específico identificado por su ID.<br>

Puedes crear un nuevo coche enviando una solicitud POST a /api/cars/.<br>
Método HTTP: POST<br>
Descripción: Esta ruta permite crear un nuevo coche en el sistema.<br>

Puedes actualizar un coche existente enviando una solicitud PUT a /api/cars/"id"/.<br>
Método HTTP: PUT<br>
Descripción: Esta ruta permite actualizar los detalles de un coche existente identificado por su ID.<br>

Puedes eliminar un coche existente enviando una solicitud DELETE a /api/cars/"id"/.<br>
Método HTTP: DELETE<br>
Descripción: Esta ruta permite eliminar un coche existente identificado por su ID.<br>

La ruta /api/car_features/ devuelve todas las características de los coches.<br>
Método HTTP: GET<br>
Descripción: Esta ruta devuelve una lista de todas las características de los coches en el sistema.<br>

Puedes actualizar una característica de un coche existente enviando una solicitud PUT a /api/car_features/"id"/update/.<br>
Método HTTP: PUT<br>
Descripción: Esta ruta permite actualizar una característica de un coche existente identificada por su ID.<br>

Puedes eliminar una característica de un coche existente enviando una solicitud DELETE a /api/car_features/"id"/delete/.<br>
Método HTTP: DELETE<br>
Descripción: Esta ruta permite eliminar una característica de un coche existente identificada por su ID.<br>

La ruta /api/car_info/ devuelve toda la información de los coches.<br>
Método HTTP: GET<br>
Descripción: Esta ruta devuelve una lista de toda la información de los coches en el sistema.<br>

Puedes actualizar la información de un coche existente enviando una solicitud PUT a /api/car_info/"id"/update/.<br>
Método HTTP: PUT<br>
Descripción: Esta ruta permite actualizar la información de un coche existente identificada por su ID.<br>

Puedes eliminar la información de un coche existente enviando una solicitud DELETE a /api/car_info/"id"/delete/.<br>
Método HTTP: DELETE<br>
Descripción: Esta ruta permite eliminar la información de un coche existente identificada por su ID.<br>
