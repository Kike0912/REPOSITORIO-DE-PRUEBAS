# Guía de Pruebas y Comandos Básicos de Git (Repositorio Clonado)

Hice un cambio xd 
hice oltra cosa 
## 1. Verifica la Configuración

- **Verifica tu nombre y correo configurados:**
  ```bash
  git config user.name
  git config user.email
  git config --list
  ```

## 2. Estado del Repositorio

- **Verifica el estado actual del repositorio:**
  ```bash
  git status
  ```
## B. Caso especial donde clonaste un repositorio que ya tenia un reapdme lo cambiaste y te dice que el read me esta modificado pero no a pasado 

 ```bash
  git add README.md
  git commit -m "Describe aquí el cambio realizado"
  git push 
  git status 
  ```
# haciendo actualizaciones massivas del codigo `git add .`

 ```bash
    git add . 
    git commit -m "commit massivo añade y actualiza"
    git push 
    git status 
  ``` 

  # Opciones comunes de Git con `-letra`

| Opción | Descripción                                               | Ejemplo                                      |
|--------|-----------------------------------------------------------|----------------------------------------------|
| -m     | Especifica el mensaje del commit                          | git commit -m "Mensaje del commit"           |
| -a     | Incluye todos los archivos modificados en el commit       | git commit -a -m "Commit rápido"             |
| -d     | Elimina una rama                                          | git branch -d nombre-rama                    |
| -b     | Crea una nueva rama y cambia a ella                       | git checkout -b nueva-rama                   |
| -u     | Establece upstream (rama de seguimiento remota)           | git push -u origin main                      |
| -v     | Muestra información detallada (verbose)                   | git status -v                                |
| -f     | Forzar una acción (por ejemplo, forzar un push o delete)  | git push -f origin main                      |

> Usa `git help <comando>` para ver todas las opciones disponibles para cada comando.

## 3. Flujo Básico de Trabajo

- **Crea un archivo y agrégalo al área de staging:**
  ```bash
  echo "Hola Git" > archivo.txt
  git add archivo.txt
  git status
  ```

- **Confirma los cambios (commit):**
  ```bash
  git commit -m "Agrega archivo.txt de prueba"
  ```

- **Ver historial de commits:**
  ```bash
  git log --oneline (este esta mucho mas resumido)   

  o tambien

  git log  (esto muestra con mucho mas detalle el historial)
  ```

## 4. Trabajando con Ramas

- **Crea una nueva rama y cámbiate a ella:**
  ```bash
  git branch nueva-rama
  git checkout nueva-rama
  ```

- **Haz un cambio en la nueva rama y confírmalo:**
  ```bash
  echo "Cambio en nueva rama" >> archivo.txt
  git add archivo.txt
  git commit -m "Cambio en nueva rama"
  ```

  - **Subir la rama creada :**
   ```bash
   git push -u origin nueva-rama 
   ```
- **:**


- **Vuelve a la rama principal y combina los cambios:**
  ```bash
  git merge main (desde la rama donde quieres traer)
  ```

## 5. Deshacer Cambios

- **Deshaz cambios en el área de staging:**
  ```bash
  git reset archivo.txt
  ```

- **Deshaz cambios en el archivo (antes de hacer commit):**
  ```bash
  git checkout -- archivo.txt
  ```

## 6. Trabajando con Remotos

- **Descarga cambios del remoto:**
  ```bash
  git pull origin main
  ```

- **Envía tus cambios al remoto:**
  ```bash
  git push origin main
  ```

## 7. Otros Comandos Útiles

- **Ver ramas disponibles:**
  ```bash
  git branch
  ```

- **Ver diferencias entre archivos:**
  ```bash
  git diff
  ```

- **Eliminar una rama:**
  ```bash
  git branch -d nueva-rama
  ```

---

## Pruebas Sugeridas

1. Crea un archivo, agrégalo y haz commit.
2. Crea una rama, haz cambios y combínalos con la rama principal.
3. Prueba a deshacer cambios antes y después de hacer commit.
4. Haz un `pull` y un `push` para sincronizar con el repositorio remoto.
5. Elimina una rama y verifica el historial.

> **Consejo:** Usa `git help <comando>` para ver la ayuda de cada comando.

¡Practica cada comando y observa cómo cambia el estado de tu repositorio!