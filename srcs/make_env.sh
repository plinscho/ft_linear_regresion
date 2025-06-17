#!/bin/bash

# Upgrade pip (dentro del entorno virtual)
python3 -m pip install --user --upgrade pip

# Instalar dependencias necesarias del sistema si estás en Debian/Ubuntu
if command -v apt-get &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-venv python3-tk
fi

# Crear entorno virtual en la carpeta raíz del proyecto
python3 -m venv ./virtual_env

# Activar entorno virtual
source ./virtual_env/bin/activate

# Verificar que el entorno fue activado correctamente
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Entorno virtual activado correctamente."

    # Ruta correcta al archivo requirements.txt
    if [[ -f "srcs/requirements.txt" ]]; then
        pip install -r srcs/requirements.txt
    else
        echo "⚠️  requirements.txt no encontrado en srcs/"
    fi
else
    echo "❌ Fallo al activar entorno virtual."
fi

