load "data/cursos_online.csv";
filter column "calificacion_final" == 54.7;
aggregate AVERAGE column "porcentaje_avance";
aggregate SUM column "calificacion_final";
print;