# Guía de colaboración

Este proyecto se desarrolla en equipo siguiendo la metodología **Gitflow**.

## Ramas

| Rama | Uso |
|---|---|
| `main` | Versión estable de la aplicación |
| `develop` | Rama de desarrollo (rama por defecto) |
| `bugfix/...` | Corrección de errores |
| `feature/...` | Nuevas funcionalidades o mejoras |
| `docs/...` | Cambios en la documentación |

Las ramas de trabajo se crean siempre a partir de `develop`.

## Flujo de trabajo

1. Registrar la tarea como **Issue** (con la plantilla de error si es un bug) y asignarla.
2. Actualizar `develop` y crear una rama propia:

   ```bash
   git checkout develop
   git pull
   git checkout -b bugfix/nombre-corto
   ```

3. Hacer los cambios, probarlos en local y subirlos:

   ```bash
   git add .
   git commit -m "Descripción clara del cambio"
   git push -u origin bugfix/nombre-corto
   ```

4. Abrir un **Pull Request hacia `develop`**, rellenando la plantilla e indicando
   `Closes #N` con el número de la Issue.
5. Solicitar la revisión de un compañero en **Reviewers**.
6. El revisor comenta, aprueba o pide cambios, y hace el merge tras aprobarlo.

## Normas

- Cada integrante utiliza su propia cuenta de GitHub.
- Todas las modificaciones se hacen en ramas independientes.
- Cada tarea debe tener una Issue asociada.
- Los Pull Requests deben incluir toda la información de la plantilla.
- Nadie revisa ni aprueba sus propios cambios.
- Las observaciones y decisiones quedan registradas en GitHub (comentarios en Issues y Pull Requests).
- Los cambios se revisan antes de incorporarse a la rama principal.

## Revisiones

Las revisiones se reparten en círculo, de forma que todos revisan y todos son revisados.

## Publicación en `main`

Cuando todos los cambios están fusionados en `develop`, se abre un Pull Request
de `develop` a `main`, revisado por un compañero distinto del que lo abre.
