load "data/cursos_online.csv";
filter column "calificacion_final" > 32.9 OR;
filter column "modalidad" != "Autodirigida" AND;
filter column "curso" != "Desarrollo Web Full Stack";
aggregate SUM column "calificacion_final";
aggregate SUM column "porcentaje_avance";
print;