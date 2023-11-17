# Recipe Finder API

Bienvenido a nuestro proyecto de API para Recetas de Cocina. Este proyecto proporciona una plataforma robusta y versátil para la gestión de recetas culinarias, permitiendo a los usuarios realizar diversas acciones relacionadas con la cocina. Aquí hay un vistazo a las principales funcionalidades del API:

**Autenticación de Usuarios**: El API permite la creación de usuarios y facilita el inicio de sesión, proporcionando una experiencia personalizada para los usuarios registrados.

**Gestión de Ingredientes**: Los usuarios pueden crear y gestionar una variedad de ingredientes que luego se pueden utilizar en la creación de recetas.

**Categorías de Recetas**: El API ofrece la posibilidad de crear y organizar recetas mediante la asignación de categorías, facilitando la búsqueda y navegación de los usuarios.

**Operaciones Complejas sobre Recetas**: Los usuarios pueden realizar diversas operaciones sobre las recetas, como crear, editar, listar y eliminar. Además, el API está diseñado para admitir futuras funcionalidades que ampliarán la gama de acciones disponibles.

**Calificación de Recetas**: Los usuarios tienen la capacidad de calificar las recetas, proporcionando una retroalimentación valiosa sobre la calidad y el gusto de las preparaciones culinarias.

**Multimedia en Recetas**: Al crear una receta, los usuarios pueden enriquecer su contenido con imágenes adicionales, videos detallando el proceso de preparación y una guía paso a paso para facilitar la reproducción precisa.

Este proyecto está enfocado en ofrecer una experiencia integral para los entusiastas de la cocina, ya sean principiantes o chefs experimentados. Explora las diversas funcionalidades que ofrecemos y disfruta del viaje culinario que nuestro API hace posible. ¡Esperamos que encuentres inspiración y comodidad en la preparación de tus platos favoritos!

## Requisitos

Asegúrate de tener instaladas las siguientes dependencias antes de ejecutar el proyecto:

- asgiref==3.7.2
- backports.zoneinfo==0.2.1
- blessings==1.7
- click==7.1.2
- curtsies==0.3.4
- dj-rest-auth==5.0.2
- Django==4.1
- django-cli-g73==0.2.0
- django-cors-headers==4.3.1
- djangorestframework==3.14.0
- enquiries==0.1.0
- gunicorn==21.2.0
- packaging==23.2
- Pillow==10.1.0
- psycopg2==2.9.9
- psycopg2-binary==2.9.9
- pyfiglet==0.8.post1
- PyMySQL==1.1.0
- python-decouple==3.8
- pytz==2023.3.post1
- six==1.15.0
- sqlparse==0.4.4
- typing_extensions==4.8.0
- wcwidth==0.2.5
- whitenoise==6.6.0

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu_usuario/recipe_finder_backend.git
cd recipe_finder_backend
```

2. Instala las dependiencias:
```bash
pip install -r requirements.txt
```

3. Realiza las migraciones de la base de datos
```bash
python manage.py migrate
```

## Configuracion

1. Crea un archivo .env en el directorio principal del proyecto y configura las variables de entorno necesarias. Puedes usar el archivo .env.example como referencia.

2. Configura la base de datos en el archivo settings.py.

## Uso
Ejecuta el servidor de desarrollo:
```bash
python manage.py runserver
```
El servidor estará disponible en http://localhost:8000/.

## API

### Documentación

La documentación completa de la API se encuentra [aquí](enlace-a-documentacion).

### Autenticación

Para utilizar las funcionalidades protegidas, los usuarios deben registrarse y obtener un token de autenticación.

- **Registro de Usuario:**
  - **Endpoint:** `POST /api/register/`
  - **Cuerpo de la Solicitud:**
    ```json
    {
      "name": "nombre",
      "email": "correo@ejemplo.com",
      "password": "contraseña_segura",
      "birthday": 1999-02-05,
      "profile_picture": "photo.png"
    }
    ```
  - **Respuesta Exitosa:**
    ```json
    {
      "message": "Usuario registrado exitosamente."
    }
    ```

- **Inicio de Sesión:**
  - **Endpoint:** `POST /api/auth/login/`
  - **Cuerpo de la Solicitud:**
    ```json
    {
      "username": "correo@ejemplo.com",
      "password": "contraseña"
    }
    ```
  - **Respuesta Exitosa:**
    ```json
    {
      "token": "token_de_autenticacion"
    }
    ```

### Gestión de Ingredientes

- **Listar Ingredientes:**
  - **Endpoint:** `GET /api/ingredients/`

- **Crear Ingrediente:**
  - **Endpoint:** `POST /api/ingredients/`
  - **Cuerpo de la Solicitud:**
    ```json
    {
      "name": "Nombre del Ingrediente"
    }
    ```

### Categorías de Recetas

- **Listar Categorías:**
  - **Endpoint:** `GET /api/categories/`

- **Crear Categoría:**
  - **Endpoint:** `POST /api/categories/`
  - **Cuerpo de la Solicitud:**
    ```json
    {
      "name": "Nombre de la Categoría"
    }
    ```

### Operaciones sobre Recetas

- **Listar Recetas:**
  - **Endpoint:** `GET /api/recipes/`

- **Crear Receta:**
  - **Endpoint:** `POST /api/recipes/`
  - **Cuerpo de la Solicitud:**
    ```json
    {
      "title": "Título de la Receta",
      "ingredients": [1, 2, 3],
      "category": 1,
      "steps": ["Paso 1", "Paso 2"],
      "images": ["imagen1.jpg", "imagen2.jpg"],
      "video": "enlace_al_video.mp4"
    }




