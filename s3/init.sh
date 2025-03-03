#!/bin/sh
echo "Esperando a que MinIO esté listo..."

echo "MinIO está listo, inicializando configuración..."

# Configurar alias para MinIO Client (mc)
mc alias set local http://localhost:9000 $S3_ACCESS_KEY $S3_SECRET_KEY

# Crear el bucket si no existe
mc mb local/$S3_BUCKET || true

# Hacer el bucket público
mc anonymous set public local/$S3_BUCKET

echo "✅ Bucket $S3_BUCKET creado y configurado como público."