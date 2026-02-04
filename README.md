# Práctica: Infraestructura de Microservicios, Caché y Gestión de Versiones

## 1. Descripción
Este proyecto implementa una arquitectura de microservicios para la empresa "Cloud-Fast". Se ha diseñado un entorno seguro y de alto rendimiento utilizando **Docker**, **Nginx** como proxy inverso con caché de nivel 1, y **Redis** como caché de nivel 2.

## 2. Diagrama de Arquitectura
La infraestructura se basa en una red privada interna donde el único punto de entrada es el Proxy Nginx (Puerto 80). El backend (API) y la base de datos (Redis) están aislados del exterior.

![Diagrama de Arquitectura](diagrama.png)

## 3. Instrucciones de Despliegue
Para levantar este entorno en un servidor local o remoto, siga estos pasos:

```bash
# 1. Clonar el repositorio
git clone [https://github.com/joseluisinformatica24-debug/jjimban-seguridad.git](https://github.com/joseluisinformatica24-debug/jjimban-seguridad.git)

# 2. Acceder al directorio
cd jjimban-seguridad

# 3. Desplegar los contenedores
docker-compose up -d --build
