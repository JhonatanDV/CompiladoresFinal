load "data/cursos_online.csv";
filter column "porcentaje_avance" <= 1 OR;
filter column "fecha_fin" <= 2022-01-09;
aggregate AVERAGE column "calificacion_final";
aggregate COUNT column "fecha_fin";
print;