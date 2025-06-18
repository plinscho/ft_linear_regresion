#!/bin/bash

python3 -m pip install --user --upgrade pip

if command -v apt-get &> /dev/null; then
    apt-get update
    apt-get install -y python3-venv python3-tk
fi

python3 -m venv ./virtual_env
source ./virtual_env/bin/activate

if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "✅ Entorno virtual activado correctamente."
    if [[ -f "srcs/requirements.txt" ]]; then
        pip install -r srcs/requirements.txt
    else
        echo "⚠️  requirements.txt no encontrado en srcs/"
    fi
else
    echo "❌ Fallo al activar entorno virtual."
    echo "ℹ️  Usa: source srcs/make_env.sh para activar el entorno en tu shell."
fi

