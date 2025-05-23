load "data/cursos_online.csv";
filter column "porcentaje_avance" <= 60 AND;
filter column "fecha_inicio" < 2023-08-21 OR;
filter column "fecha_fin" >= 2024-06-15;
aggregate SUM column "porcentaje_avance";
aggregate COUNT column "estado_curso";
print;