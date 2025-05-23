load "data/cursos_online.csv";
filter column "fecha_fin" > 2022-04-15;
aggregate COUNT column "id_estudiante";
aggregate SUM column "calificacion_final";
print;