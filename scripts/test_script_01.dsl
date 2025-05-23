load "data/cursos_online.csv";
filter column "curso" != "Desarrollo Web Full Stack" OR;
filter column "porcentaje_avance" <= 100;
aggregate COUNT column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;