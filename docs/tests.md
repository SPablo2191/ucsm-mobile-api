### Casos de Prueba para la API REST

#### 1. **Inicio de Sesión**

- **Endpoint:** `POST api/login`
- **Descripción:** Permite a los usuarios iniciar sesión en el sistema proporcionando el documento de identificación y la contraseña.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **1.1** | Ingreso exitoso con credenciales válidas | `{ "identification_document": "12345678", "password": "correct_password" }` | Respuesta HTTP 200, Token de sesión válido retornado. |
| **1.2** | Intento de inicio de sesión con credenciales inválidas | `{ "identification_document": "12345678", "password": "wrong_password" }` | Respuesta HTTP 401, Mensaje de error de credenciales inválidas. |
| **1.3** | Intento de inicio de sesión con documento de identificación inválido | `{ "identification_document": "invalid_id", "password": "correct_password" }` | Respuesta HTTP 404, Mensaje de error indicando que el usuario no existe. |
| **1.4** | Intento de inicio de sesión sin proporcionar una contraseña | `{ "identification_document": "12345678", "password": "" }` | Respuesta HTTP 400, Mensaje de error indicando que la contraseña es requerida. |

#### 2. **Deuda**

- **Endpoint:** `GET api/debts/get-debt/?enrollment_id=<uuid:id>`
- **Descripción:** Recupera la deuda de un curso específico y sus cuotas asociadas.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **2.1** | Recuperar deuda con un `enrollment_id` válido | `?enrollment_id=valid_uuid` | Respuesta HTTP 200, Detalles de la deuda y cuotas asociadas para el curso. |
| **2.2** | Recuperar deuda con un `enrollment_id` inválido | `?enrollment_id=invalid_uuid` | Respuesta HTTP 404, Mensaje de error indicando que el curso no existe. |
| **2.3** | Recuperar deuda sin un `enrollment_id` proporcionado | `?enrollment_id=` | Respuesta HTTP 400, Mensaje de error indicando que el `enrollment_id` es requerido. |
| **2.4** | Recuperar deuda sin token de sesión válido | `?enrollment_id=valid_uuid` (sin header de autorización) | Respuesta HTTP 401, Mensaje de error indicando que se requiere autenticación. |

#### 3. **Inscripción**

- **Endpoints:** 
  - `GET api/enrollments/?identification_document=<string:dni>`
  - `GET api/enrollments/<string:id>`

- **Descripción:** Obtiene la lista de cursos de un estudiante y detalles de un curso específico.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **3.1** | Obtener listado de cursos de un estudiante con `dni` válido | `?identification_document=12345678` | Respuesta HTTP 200, Lista de cursos en los que el estudiante está inscrito. |
| **3.2** | Obtener listado de cursos con `dni` inválido | `?identification_document=invalid_dni` | Respuesta HTTP 404, Mensaje de error indicando que el estudiante no existe. |
| **3.3** | Obtener detalles de un curso con un `id` válido | `/api/enrollments/valid_uuid` | Respuesta HTTP 200, Información detallada del curso. |
| **3.4** | Obtener detalles de un curso con un `id` inválido | `/api/enrollments/invalid_uuid` | Respuesta HTTP 404, Mensaje de error indicando que el curso no existe. |
| **3.5** | Obtener listado de cursos sin `dni` proporcionado | `?identification_document=` | Respuesta HTTP 400, Mensaje de error indicando que el `dni` es requerido. |

#### 4. **Eventos**

- **Endpoints:** 
  - `GET api/events`
  - `GET api/events/<string:id>`

- **Descripción:** Permite acceder a la lista de eventos y a los detalles de un evento en particular.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **4.1** | Obtener listado de eventos | `/api/events` | Respuesta HTTP 200, Lista de eventos disponibles. |
| **4.2** | Obtener detalles de un evento con un `id` válido | `/api/events/valid_event_id` | Respuesta HTTP 200, Detalles del evento. |
| **4.3** | Obtener detalles de un evento con un `id` inválido | `/api/events/invalid_event_id` | Respuesta HTTP 404, Mensaje de error indicando que el evento no existe. |
| **4.4** | Obtener listado de eventos con un token de sesión no válido | `/api/events` (sin header de autorización válido) | Respuesta HTTP 401, Mensaje de error indicando que se requiere autenticación. |

#### 5. **Semestres**

- **Endpoints:** 
  - `GET api/semesters`
  - `GET api/semesters/<string:id>`

- **Descripción:** Proporciona una lista de semestres disponibles y detalles de un semestre específico.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **5.1** | Obtener lista de semestres disponibles | `/api/semesters` | Respuesta HTTP 200, Lista de todos los semestres disponibles. |
| **5.2** | Obtener detalles de un semestre con un `id` válido | `/api/semesters/valid_semester_id` | Respuesta HTTP 200, Información detallada del semestre. |
| **5.3** | Obtener detalles de un semestre con un `id` inválido | `/api/semesters/invalid_semester_id` | Respuesta HTTP 404, Mensaje de error indicando que el semestre no existe. |
| **5.4** | Obtener lista de semestres con un token de sesión no válido | `/api/semesters` (sin header de autorización válido) | Respuesta HTTP 401, Mensaje de error indicando que se requiere autenticación. |

#### 6. **Perfil del Estudiante**

- **Endpoint:** `GET api/students/<string:id>`

- **Descripción:** Permite obtener el perfil completo de un estudiante.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **6.1** | Obtener perfil de un estudiante con un `id` válido | `/api/students/valid_student_id` | Respuesta HTTP 200, Detalles del perfil del estudiante. |
| **6.2** | Obtener perfil de un estudiante con un `id` inválido | `/api/students/invalid_student_id` | Respuesta HTTP 404, Mensaje de error indicando que el estudiante no existe. |
| **6.3** | Obtener perfil del estudiante con un token de sesión no válido | `/api/students/valid_student_id` (sin header de autorización válido) | Respuesta HTTP 401, Mensaje de error indicando que se requiere autenticación. |

#### 7. **Registro de Materias**

- **Endpoints:** 
  - `GET api/subject-registrations/?enrollment_id=<uuid:id>`
  - `GET api/subject-registrations/<string:id>`
  - `GET api/subject-registrations/get-remaining-subjects/?enrollment_id=<uuid:id>`
  - `GET api/subject-registrations/get-statistics/?enrollment_id=<uuid:id>`

- **Descripción:** Maneja la información de materias inscritas, detalles de una materia, materias restantes y estadísticas de materias.

| Caso de Prueba | Descripción | Datos de Entrada | Resultado Esperado |
|----------------|-------------|------------------|---------------------|
| **7.1** | Obtener materias inscritas con `enrollment_id` válido | `?enrollment_id=valid_uuid` | Respuesta HTTP 200, Lista de materias en las que el estudiante está inscrito. |
| **7.2** | Obtener materias inscritas con `enrollment_id` inválido | `?enrollment_id=invalid_uuid` | Respuesta HTTP 404, Mensaje de error indicando que el curso no existe. |
| **7.3** | Obtener detalles de una materia con un `id` válido | `/api/subject-registrations/valid_subject_id` | Respuesta HTTP 200, Información detallada de la materia. |
| **7.4** | Obtener detalles de una materia con un `id` inválido | `/api/subject-registrations/invalid_subject_id` | Respuesta HTTP 404, Mensaje de error indicando que la materia no existe. |
| **7.5** | Obtener materias restantes con un `enrollment_id` válido | `?enrollment_id=valid_uuid` | Respuesta HTTP 200, Lista de materias