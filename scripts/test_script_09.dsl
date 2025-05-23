load "data/cursos_online.csv";
filter column "porcentaje_avance" < 70 OR;
filter column "fecha_fin" >= 2022-03-11 AND;
filter column "estado_curso" == "Cancelado";
aggregate COUNT column "estado_curso";
aggregate SUM column "porcentaje_avance";
print;