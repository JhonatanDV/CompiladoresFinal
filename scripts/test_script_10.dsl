load "data/cursos_online.csv";
filter column "calificacion_final" != 4.4;
aggregate COUNT column "modalidad";
aggregate AVERAGE column "calificacion_final";
print;