load "data/cursos_online.csv";
filter column "id_estudiante" != "EST0053" AND;
filter column "modalidad" != "Híbrida" OR;
filter column "fecha_fin" <= 2022-04-21;
aggregate SUM column "calificacion_final";
print;