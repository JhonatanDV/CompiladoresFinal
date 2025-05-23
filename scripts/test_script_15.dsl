load "data/cursos_online.csv";
filter column "fecha_fin" >= 2022-06-28;
aggregate AVERAGE column "calificacion_final";
print;