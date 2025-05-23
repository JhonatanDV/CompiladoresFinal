load "data/cursos_online.csv";
filter column "fecha_fin" == 2022-12-25 OR;
filter column "fecha_fin" < 2022-09-13;
aggregate SUM column "porcentaje_avance";
aggregate COUNT column "estado_curso";
print;