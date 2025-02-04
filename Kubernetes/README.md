Pasos para configurar K3s usando Docker:
1️⃣ Abre Docker
Asegúrate de que Docker Desktop esté abierto y funcionando. Si no lo tienes, instálalo aquí.
2️⃣ Descargar la imagen de K3s
Vamos a utilizar una imagen Docker que ejecuta K3s. Abre la terminal de tu sistema operativo y ejecuta este comando para descargar la imagen de K3s.

bash
Copiar
Editar
docker pull rancher/k3s:v1.25.4-k3s1
Esto descargará la imagen de K3s desde Docker Hub.

3️⃣ Ejecutar K3s en un contenedor Docker
Ahora, vamos a crear un contenedor que ejecute K3s. Ejecuta este comando en la terminal:

bash
Copiar
Editar
docker run -d --privileged --name k3s-server -p 6443:6443 rancher/k3s:v1.25.4-k3s1
Explicación:

-d ejecuta el contenedor en segundo plano.
--privileged permite acceso de root para que K3s funcione correctamente.
--name k3s-server es el nombre que le damos al contenedor.
-p 6443:6443 mapea el puerto 6443 (el puerto por defecto de K3s) al host para acceder al clúster.
4️⃣ Verificar que K3s está corriendo
Para asegurarte de que todo esté funcionando, puedes ejecutar este comando para ver los contenedores en ejecución:

bash
Copiar
Editar
docker ps
Deberías ver algo como esto:

plaintext
Copiar
Editar
CONTAINER ID   IMAGE                     COMMAND                  CREATED       STATUS       PORTS                    NAMES
abcd1234       rancher/k3s:v1.25.4-k3s1   "/bin/k3s server"        10 seconds ago Up 9 seconds  0.0.0.0:6443->6443/tcp   k3s-server
5️⃣ Configurar kubectl para interactuar con el clúster
Ahora necesitamos configurar kubectl (la herramienta de línea de comandos para Kubernetes) para conectarnos al clúster que acabamos de crear.

Instala kubectl si aún no lo tienes:
Instrucciones para instalar kubectl

Obtén la configuración de K3s desde el contenedor:

Ejecuta este comando para obtener el archivo de configuración de Kubernetes y configurarlo:

bash
Copiar
Editar
docker exec k3s-server cat /etc/rancher/k3s/k3s.yaml
Esto te dará un archivo YAML. Copia todo el contenido.

Configura kubectl para usar ese archivo:

Crea un archivo en tu máquina con el nombre config y pega allí lo que copiaste.

Luego, configura kubectl para usar este archivo como configuración:

bash
Copiar
Editar
export KUBEVIRT_KUBECTL_CONFIG=/path/to/config
O si prefieres hacerlo permanentemente, puedes añadirlo a tu archivo .bashrc o .zshrc (dependiendo del shell que uses).

6️⃣ Verificar el clúster
Ahora que todo está configurado, puedes verificar que tu clúster de K3s está funcionando correctamente con:

bash
Copiar
Editar
kubectl get nodes
Este comando debería mostrarte información sobre tu clúster y el nodo que acabamos de crear.

¡Y listo! Con eso, ya tendrías K3s ejecutándose sobre Docker de manera bastante ligera, y listo para empezar a desplegar aplicaciones de Kubernetes.

