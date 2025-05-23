load "data/cursos_online.csv";
filter column "estado_curso" != "Pausado" OR;
filter column "porcentaje_avance" < 53 AND;
filter column "estado_curso" != "Activo";
aggregate SUM column "porcentaje_avance";
print;