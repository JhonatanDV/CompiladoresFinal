load "data/cursos_online.csv";
filter column "estado_curso" != "Cancelado" AND;
filter column "fecha_fin" <= 2024-04-08;
aggregate SUM column "porcentaje_avance";
aggregate COUNT column "fecha_inicio";
print;