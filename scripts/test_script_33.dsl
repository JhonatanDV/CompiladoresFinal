load "data/cursos_online.csv";
filter column "fecha_fin" >= 2024-06-14 OR;
filter column "porcentaje_avance" >= 90 AND;
filter column "fecha_fin" == 2023-09-09;
aggregate AVERAGE column "porcentaje_avance";
aggregate SUM column "calificacion_final";
print;