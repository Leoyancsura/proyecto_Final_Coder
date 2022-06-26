# proyecto_Final_Coder
## **Crear web similar a un blog.**

> - Se deberá realizar en duplas o tríos, crearás una aplicación web estilo blog programada en Python / Django. Esta web tendrá **admin**, **perfiles**, **registró**, **páginas** y **formularios**.
> - La entrega se realizará enviando el **link a GitHub**, en el **readme** de Github deberá estar el nombre completo de los tres/dos participantes y una descripción de dos o tres renglones contando qué hizo cada uno.
> - En el github debe haber un **video o link a vídeo donde nos muestran su web funcionando en no más de diez minutos**. 
> - Dentro del Github deberá existir una carpeta con por lo menos 3 casos de pruebas debidamente documentados. **(opcional)**
> - Contar con algún acceso visible a la **vista de "Acerca de mí"** donde se contará acerca de los dueños de la página manejado en el route about/.  (En castellano un “acerca de mí” que hable un poco de los creadores de la web y del proyecto).
> - Contar con algún acceso visible a la vista de blogs que debe alojarse en el route pages/. (Es decir un html que permite listar todos los blogs de la BD, con una información mínima de dicho blog).
> - Acceder a una pantalla que contendrá las páginas. Al clickear en “Leer más” debe navegar al detalle de la page mediante un route pages/<pageId>. (O sea al hacer click se ve más detalle de lo que se veía en el apartado anterior).
> - Si no existe ninguna página mostrar un "No hay páginas aún". (Aclarando, si en la página hacemos clic en algún lugar que no existe que diga eso, o que lleve a un html con esos mensaje, no dejar botones que no responden).
> - Para crear, editar o borrar las fotos debes estar registrado como Administrador.
> - Cada blog, es decir cada model Blog debe tener como mínimo, un título, subtítulo, cuerpo, autor, fecha y una imagen (mínimo y obligatorio, puede tener más).

# **GITHUB COMANDOS**
## create a new repository on the command line
    echo "# ProyectoFinal" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/Leoyancsura/ProyectoFinal.git
    git push -u origin main

 ## push an existing repository from the command line
    git remote add origin https://github.com/Leoyancsura/ProyectoFinal.git
    git branch -M main
    git push -u origin main
