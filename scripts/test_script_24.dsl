load "data/cursos_online.csv";
filter column "calificacion_final" <= 60.5;
aggregate AVERAGE column "porcentaje_avance";
print;