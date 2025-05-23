load "data/cursos_online.csv";
filter column "calificacion_final" > 64.2;
aggregate COUNT column "modalidad";
aggregate AVERAGE column "calificacion_final";
print;