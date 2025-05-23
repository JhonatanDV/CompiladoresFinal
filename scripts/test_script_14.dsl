load "data/cursos_online.csv";
filter column "curso" != "Machine Learning" OR;
filter column "estado_curso" != "Completado" OR;
filter column "fecha_fin" > 2022-01-20;
aggregate AVERAGE column "calificacion_final";
print;