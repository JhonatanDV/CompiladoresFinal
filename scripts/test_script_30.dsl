load "data/cursos_online.csv";
filter column "curso" != "Python Básico" AND;
filter column "fecha_fin" > 2022-11-15;
aggregate AVERAGE column "calificacion_final";
aggregate COUNT column "modalidad";
print;