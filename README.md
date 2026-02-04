# Práctica 10: Infraestructura de Microservicios, Caché y Gestión de Versiones

## 1. Descripción
[cite_start]Este proyecto consiste en el despliegue de una arquitectura de microservicios para la empresa "Cloud-Fast"[cite: 56]. [cite_start]El objetivo es implementar un entorno seguro y eficiente utilizando contenedores Docker, con un enfoque en tres pilares: Seguridad Perimetral, Alto Rendimiento y Buenas Prácticas DevOps[cite: 57, 58].

## 2. Diagrama de Arquitectura
[cite_start]El sistema utiliza una red privada interna (172.x.x.x) donde solo el Proxy Nginx es accesible desde el exterior[cite: 40, 66].

![Diagrama de Arquitectura](https://via.placeholder.com/600x400?text=Sube+aquí+la+imagen+del+croquis)
[cite_start]*(Nota: Exporta el croquis de la página 4 del PDF como PNG y súbelo a tu repositorio con el nombre `arquitectura.png` [cite: 99])*

## 3. Instrucciones de Despliegue
[cite_start]Para clonar y levantar el entorno completo, ejecute los siguientes comandos en su terminal[cite: 100, 118]:

```bash
# Clonar el repositorio
git clone <URL_DE_TU_REPOSITORIO>

# Entrar en la carpeta
cd nombre-repositorio

# Levantar la infraestructura
docker-compose up -d --build
```
