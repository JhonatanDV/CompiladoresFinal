load "data/cursos_online.csv";
filter column "calificacion_final" <= 49.7 OR;
filter column "calificacion_final" != 82.9 OR;
filter column "fecha_fin" > 2024-07-22;
aggregate COUNT column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;