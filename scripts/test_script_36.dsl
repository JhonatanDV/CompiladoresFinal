load "data/cursos_online.csv";
filter column "porcentaje_avance" != 89 AND;
filter column "calificacion_final" == 86.8;
aggregate AVERAGE column "calificacion_final";
print;