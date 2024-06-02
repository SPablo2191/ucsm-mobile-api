# Endpoints 
## Modulos 🚨
- [Auth](#auth)
- [Debt](#debt)
- [Enrollment](#enrollment)
- [Event](#event)
- [Semester](#semester)
- [Student](#student)
- [Subject Registration](#subject-registration)

### Auth

| Método | Path | Descripción |
| ------ | -------- | ----------- |
| POST    | api/login | Inicio de sesión |
| POST    | api/logout | Finalizar sesión |

**Inicio de sesión**

se tiene que enviar en la request el siguiente body:
```json
{
  "identification_document": "string",
  "password": "string"
}
```

### Debt

| Método | Path | Descripción |
| ------ | -------- | ----------- |
| GET   | api/debts/get-debt/?enrollment_id=<uuid:id> | Recuperar la deuda de un curso en particular y sus cuotas |

### Enrollment

| Método | Path                     | Descripción                                 |
| ------ | ------------------------ | ------------------------------------------- |
| GET    | api/enrollments/?identification_document=<string:dni>           | Recuperar el listado de cursos de un estudiante |
| GET    | api/enrollments/<string:id>          | Recuperar un curso especifico |
### Event

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| GET    | api/events            | Recuperar el listado de eventos     |
| GET    | api/events/<string:id>            | Recuperar un evento en particular     |

### Semester

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| GET  | api/semesters  |Recuperar el listado de semestres              |
| GET | api/semesters/<string:id>   | Recuperar un semestre en particular   |

### Student

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| GET | api/students/<string:id>   | Recuperar el perfil de un estudiante  |

### Subject Registration

| Método | Path                    | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| GET | api/subject-registrations/?enrollment_id=<uuid:id>   | Recuperar las materias inscriptas  |
| GET | api/subject-registrations/<string:id>   | Recuperar una materia en particular |
| GET | api/subject-registrations/get-remaining-subjects/?enrollment_id=<uuid:id>   | Recuperar listado de materias restantes por cursar  |
| GET | api/subject-registrations/get-statistics/?enrollment_id=<uuid:id>   | Obtener total de materias aprobadas y restantes  |

