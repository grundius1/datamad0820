#!/bin/bash

#exercise 1: imprime en consola `Hello World`.
echo "Hello World"

# ejercicio2: Crea un directorio nuevo llamado `new_dir`.
mkdir new_dir

#ejercicio3: Elimina ese directorio.
rm -r new_dir

#ejercicio4: Copia el archivo `sed.txt` dentro de la carpeta lorem a la carpeta lorem-copy. 
cp lorem/sed.txt lorem-copy/

#ejercicio4: Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola línea mediante
cp lorem/at.txt lorem/lorem.txt lorem-copy/

#ejercicio5: Muestra el contenido del archivo `sed.txt` dentro de la carpeta lorem.
cat lorem/sed.txt

#ejercicio6: Muestra el contenido de los archivos `at.txt` y `lorem.txt` dentro de la carpeta lorem.
cat lorem/at.txt lorem/lorem.txt 

#ejercicio7: Visualiza las primeras 3 líneas del archivo `sed.txt` dentro de la carpeta lorem-copy 
cat lorem-copy/sed.txt | head -n 3

#ejercicio8: Visualiza las ultimas 3 líneas del archivo `sed.txt` dentro de la carpeta lorem-copys
cat lorem-copy/sed.txt | tail -n 3

#ejercicio9: Añade `Homo homini lupus.` al final de archivo `sed.txt` dentro de la carpeta lorem-copy.
echo "Homo homini lupus." >> lorem-copy/sed.txt 

#ejercicio10: Visualiza las últimas 3 líneas del archivo `sed.txt` dentro de la carpeta lorem-copy. Deberías ver ahora `Homo homini lupus.`. 
cat lorem-copy/sed.txt | tail -n 3

#ejercicio11: Sustituye todas las apariciones de `et` por `ET` del archivo `at.txt` dentro de la carpeta lorem-copy. Deberás usar `sed`.
sed 's/et/ET/' lorem-copy/at.txt

#ejercicio12: Encuentra al usuario activo en el sistema.
who

#ejercicio13: Encuentra dónde estás en tu sistema de ficheros.
pwd

#ejercicio14: Lista los archivos que terminan por `.txt` en la carpeta lorem.
ls -l lorem/

#ejercicio15: Cuenta el número de líneas que tiene el archivo `sed.txt` dentro de la carpeta lorem
wc -l < lorem/sed.txt
 
 #ejercicio16: Cuenta el número de **archivos** que empiezan por `lorem` que están en este directorio y en directorios internos.
find . -type f | wc -l


#ejercicio17: Encuentra todas las apariciones de `et` en `at.txt` dentro de la carpeta lorem.
grep et lorem/at.txt 

#ejercicio18: Cuenta el número de apariciones del string `et` en `at.txt` dentro de la carpeta lorem.
grep -o et lorem/at.txt | wc -l

#ejercicio19: cuenta el número de apariciones del string `et` en todos los archivos del directorio lorem-copy.
grep -R -o et lorem-copy/ | wc -l

#Bonus
#ejercicio20: Almacena en una variable `name` tu nombre.
name=Borja

#ejercicio21: Imprime esa variable.
echo $name

#ejercicio22: Crea un directorio nuevo que se llame como el contenido de la variable `name`.
mkdir "$name"

#ejercicio23: Elimina ese directorio.
rm -r "$name"

#ejercicio24: Por cada archivo dentro de la carpeta `lorem` imprime el número de carácteres que tienen sus nombres.
for i in $(ls lorem/); do echo ${i%%/}; done
for i in $(ls lorem/); do echo ${#i}; done
for i in $(ls lorem/); do echo "${i%%/} has ${#i} characters lenght"; done

#ejercicio25: Muestra los procesos de forma jerárquica que se están ejecutando en tu ordenador:
top
ps -A

#ejecrcicio26: Muestra información sobre tu procesador por pantalla
sudo lshw -c cpu

#ejercicio27: Crea 3 alias y haz que estén disponibles cada vez que inicias sesión
#sudo su –
#sudo sueradd -m usuarionuevo
#sudo passwd usuarionuevo

#ejercicio 28: Comprime las carpetas lorem y lorem-copy en un archivo llamado lorem-compressed.tar.gz



