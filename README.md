# poc_excel-api

El objetivo es usar MS Excel como interfaz de usuario para enviar y recibir datos de una API desarrollada en python y compilada como archivo **.exe**

## Requerimientos previos
### [PDM](https://pdm-project.org/en/latest/#installation)
- Instalar PDM ejecutando en la terminal de powershell:
```shell
powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"
```
- Reiniciar la terminal y verificar la instalación usando `pdm --version`
- Ejecutando el comando `pdm` mostrará los comandos disponibles

## Desarrollo
### Pasos iniciales
- Clonar el repositorio
- Crear ambiente virtual con el comando `pdm install`

### Desarrollo
- Ejecutar el comando `fastapi dev .\src\suma_api.py`
- Abrir la hoja de excel `extras\Libro1.xlsx`
    - Al hacer clic en la pestaña datos/actualizar todo, se envía una
    petición a la api
    - En la ventana del ejecutable o terminal de desarrollo debería aparecer
    el log del request enviado desde excel

## Distribución
### Generar ejecutable
- Usar comando `pdm create_exe`
    - Se crea/actualiza un archivo suma_api.exe en la carpeta *output\dist*
- O alternativamente `pyinstaller --onefile .\src\suma_api.py`

## Contribución
- Crear su propia rama de trabajo local desde `develop`: `git checkout -b my_branch`
- Hacer push de la rama de trabajo a origin `git push`
    - Si es la primera vez: `git push -u origin my_branch`
- Hacer un pull request a develop
- Hacer merge de la rama a develop