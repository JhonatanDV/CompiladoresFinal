load "data/cursos_online.csv";
filter column "plataforma" != "FreeCodeCamp" OR;
filter column "calificacion_final" != 79.1 OR;
filter column "porcentaje_avance" <= 65;
aggregate AVERAGE column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;