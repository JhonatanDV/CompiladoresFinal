load "data/cursos_online.csv";
filter column "calificacion_final" != 44.9 AND;
filter column "fecha_fin" <= 2023-11-20 AND;
filter column "calificacion_final" > 27.7;
aggregate COUNT column "fecha_fin";
aggregate AVERAGE column "calificacion_final";
print;