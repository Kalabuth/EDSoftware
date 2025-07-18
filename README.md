# API Bancaria - FastAPI con MongoDB

Una API RESTful para un sistema bancario que permite a los usuarios crear cuentas bancarias y gestionar sus saldos.

## Arquitectura

Este proyecto sigue un patrón de **arquitectura en capas** con clara separación de responsabilidades:

- **Capa API** (`app/api/`): Routers y endpoints de FastAPI
- **Capa de Servicios** (`app/services/`): Lógica de negocio
- **Capa de Repositorio** (`app/repositories/`): Capa de acceso a datos
- **Capa de Modelos** (`app/models/`): Modelos de dominio
- **Capa de Esquemas** (`app/schemas/`): Modelos Pydantic para validación

## Patrones de Diseño Utilizados

1. **Patrón Repository**: Abstrae las operaciones de base de datos
2. **Inyección de Dependencias**: Sistema de dependencias de FastAPI para conexiones de base de datos
3. **Objetos de Transferencia de Datos (DTOs)**: Esquemas Pydantic para validación de entrada/salida

## Tecnologías

- **Python 3.11+**
- **FastAPI**: Framework web moderno para construir APIs
- **MongoDB**: Base de datos NoSQL para almacenar datos de cuentas
- **Motor**: Driver asíncrono de MongoDB
- **Pydantic**: Validación de datos usando anotaciones de tipos de Python
- **Pytest**: Framework de testing
- **Docker**: Containerización

## Estructura del Proyecto

```
bank_api/
├── app/
│   ├── api/
│   │   └── accounts.py          # Endpoints de la API
│   ├── models/
│   │   └── account.py           # Modelos de dominio
│   ├── repositories/
│   │   └── account_repository.py # Capa de acceso a datos
│   ├── schemas/
│   │   └── account.py           # Esquemas Pydantic
│   └── main.py                  # Aplicación FastAPI
├── tests/
│   └── test_accounts.py         # Pruebas unitarias
├── requirements.txt             # Dependencias de Python
├── Dockerfile                   # Configuración de Docker
└── README.md                    # Este archivo
```

## Configuración e Instalación

### Prerrequisitos

- Python 3.11 o superior
- Instancia de MongoDB ejecutándose (local o en la nube)
- Docker (opcional)

### Desarrollo Local

1. **Clonar el repositorio**
   ```bash
   git clone <https://github.com/Kalabuth/EDSoftware.git>
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   ```bash
   export MONGODB_URI="mongodb://localhost:27017"
   ```

4. **Ejecutar la aplicación**
   ```bash
   python -m uvicorn app.main:app --reload
   ```

5. **Ejecutar pruebas**
   ```bash
   python -m pytest tests/ -v
   ```

### Docker

1. **Construir la imagen**
   ```bash
   docker build -t bank-api .
   ```

2. **Ejecutar el contenedor**
   ```bash
   docker run -p 8000:8000 bank-api
   ```

## Endpoints de la API

### Crear Cuenta
- **POST** `/accounts`
- **Descripción**: Crea una nueva cuenta bancaria
- **Cuerpo de la Petición**:
  ```json
  {
    "owner_name": "Juan Pérez"
  }
  ```
- **Respuesta**:
  ```json
  {
    "id": "507f1f77bcf86cd799439011",
    "message": "Account created successfully"
  }
  ```

### Actualizar Saldo
- **PATCH** `/accounts/{account_id}`
- **Descripción**: Actualiza el saldo de una cuenta existente
- **Cuerpo de la Petición**:
  ```json
  {
    "amount": 100.0
  }
  ```
- **Respuesta**:
  ```json
  {
    "id": "507f1f77bcf86cd799439011",
    "balance": 150.0
  }
  ```

### Listar Todas las Cuentas
- **GET** `/accounts`
- **Descripción**: Obtiene todas las cuentas bancarias
- **Respuesta**:
  ```json
  [
    {
      "id": "507f1f77bcf86cd799439011",
      "owner_name": "Juan Pérez",
      "balance": 150.0,
      "created_at": "2024-07-15T20:00:00.000Z"
    }
  ]
  ```

## Pruebas

El proyecto incluye pruebas unitarias completas que cubren todos los endpoints:

- Creación de cuentas
- Actualización de saldos
- Listado de cuentas

Ejecutar pruebas con:
```bash
python -m pytest tests/ -v
```

## Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **Documentación interactiva**: http://localhost:8000/docs
- **Documentación alternativa**: http://localhost:8000/redoc

## Esquema de Base de Datos

### Colección Account
```json
{
  "_id": "ObjectId",
  "owner_name": "string",
  "balance": "float",
  "created_at": "datetime"
}
```

## Manejo de Errores

La API incluye manejo apropiado de errores:

- **404**: Cuenta no encontrada
- **422**: Errores de validación
- **500**: Errores internos del servidor
