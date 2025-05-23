load "data/cursos_online.csv";
filter column "curso" == "Desarrollo Web Full Stack";
aggregate SUM column "calificacion_final";
aggregate AVERAGE column "porcentaje_avance";
print;