load "data/cursos_online.csv";
filter column "calificacion_final" == 62.0 OR;
filter column "fecha_fin" == 2022-01-15;
aggregate SUM column "porcentaje_avance";
print;