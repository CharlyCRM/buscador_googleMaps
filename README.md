# Buscador de Empresas con Google Maps

Aplicación en Python que permite buscar información de empresas utilizando la API de Google Maps y exportar los resultados a un archivo Excel.

## Datos que extrae

- Nombre de la empresa
- Horario
- Página web
- Dirección
- Teléfono de contacto

## Requisitos Previos

1. Python 3.8 o superior
2. Una API Key de Google Maps Platform con Places API habilitada

## Configuración del Proyecto

1. Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd buscador_googlemaps
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar API Key:
   - Crear un archivo `.env` en la raíz del proyecto
   - Añadir tu API key de Google Maps:
   ```
   GOOGLE_MAPS_API_KEY=tu_api_key_aquí
   ```

## Obtener API Key de Google Maps

1. Ve a [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuevo proyecto o selecciona uno existente
3. Habilita la "Places API" en la biblioteca de APIs
4. Crea una API Key en "Credenciales"
5. Copia la API Key generada al archivo `.env`

## Uso

1. Ejecutar el programa:
```bash
python main.py
```

2. Introducir el término de búsqueda cuando se solicite
3. El programa generará un archivo Excel con los resultados en la carpeta actual

## Estructura del Proyecto

```
buscador_googlemaps/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
└── src/
    ├── models/
    │   └── business.py
    ├── services/
    │   ├── google_maps_service.py
    │   └── excel_service.py
    └── interfaces/
        ├── maps_service.py
        └── storage_service.py
```
