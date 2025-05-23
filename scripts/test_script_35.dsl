load "data/cursos_online.csv";
filter column "calificacion_final" > 50.4 OR;
filter column "fecha_fin" == 2024-11-24;
aggregate SUM column "calificacion_final";
print;