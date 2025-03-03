# Legends API

Legends API es una aplicación basada en FastAPI que proporciona una API para gestionar leyendas, categorías, provincias, cantones y distritos. La aplicación utiliza SQLModel para la gestión de la base de datos y MinIO para el almacenamiento de archivos.

## Tecnologías Principales

- **FastAPI**: Framework web moderno y de alto rendimiento para construir APIs con Python 3.6+ basado en estándares como OpenAPI y JSON Schema.
- **SQLModel**: Biblioteca de Python para interactuar con bases de datos SQL utilizando Pythonic Object Relational Mapping (ORM).
- **MinIO**: Almacenamiento de objetos compatible con Amazon S3.
- **Docker**: Plataforma para desarrollar, enviar y ejecutar aplicaciones dentro de contenedores.
- **Pydantic**: Validación de datos y configuración basada en modelos de datos.

## Estructura del Proyecto

La estructura de carpetas del proyecto es la siguiente:

```plaintext
├── app
│   ├── common
│   │   ├── datetime.py
│   │   ├── __init__.py
│   │   └── singleton.py
│   ├── controllers
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── category_controller.py
│   │       ├── __init__.py
│   │       ├── legend_controller.py
│   │       └── location_controller.py
│   ├── core
│   │   ├── database.py
│   │   ├── __init__.py
│   │   ├── s3_client.py
│   │   └── settings.py
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── legend_model.py
│   ├── routes
│   │   ├── api.py
│   │   ├── category_routes.py
│   │   ├── __init__.py
│   │   ├── legend_routes.py
│   │   ├── legends_routes.py
│   │   └── location_routes.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── legend_schema.py
│   └── services
│       ├── category_service.py
│       ├── __init__.py
│       ├── legend_service.py
│       └── location_service.py
├── db
│   └── 4thewords_prueba_daren_salazar.sql
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
├── run.py
├── s3
│   └── init.sh
└── test
    ├── conftest.py
    ├── __init__.py
    ├── test_category.py
    └── test_location_routes.py
```

## Configuración del Entorno

1. Clona el repositorio:

   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Crea un archivo [.env](http://_vscodecontentref_/8) basado en [.env.example](http://_vscodecontentref_/9) y actualiza las variables de entorno según sea necesario:

   ```sh
   cp .env.example .env
   ```

3. Construye y levanta los contenedores de Docker:

   ```sh
   docker-compose up --build
   ```

4. Inicializa la base de datos:

   ```sh
   docker-compose exec app python app/core/database.py
   ```

5. Ejecuta la aplicación:

   ```sh
    docker-compose up
    o
    python3.xx run.py

   ```

La API estará disponible en `http://localhost:8080`.

## Endpoints Principales

- **Leyendas**:

  - `GET /api/v1/legend`: Obtener todas las leyendas.
  - `POST /api/v1/legend`: Crear una nueva leyenda.
  - `PUT /api/v1/legend/{id}`: Actualizar una leyenda existente.
  - `DELETE /api/v1/legend/{id}`: Eliminar una leyenda.

- **Categorías**:

  - `GET /api/v1/categories`: Obtener todas las categorías.

- **Ubicaciones**:
  - `GET /api/v1/location/cantons`: Obtener todos los cantones.
  - `GET /api/v1/location/provinces`: Obtener todas las provincias.
  - `GET /api/v1/location/districts`: Obtener todos los distritos.
