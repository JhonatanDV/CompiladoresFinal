load "data/cursos_online.csv";
filter column "estado_curso" == "Completado" OR;
filter column "fecha_inicio" >= 2022-10-01 OR;
filter column "porcentaje_avance" == 84;
aggregate AVERAGE column "porcentaje_avance";
print;