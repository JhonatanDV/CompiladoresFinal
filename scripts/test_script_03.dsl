load "data/cursos_online.csv";
filter column "modalidad" != "Autodirigida" OR;
filter column "calificacion_final" < 57.3 OR;
filter column "calificacion_final" > 61.7;
aggregate COUNT column "plataforma";
print;