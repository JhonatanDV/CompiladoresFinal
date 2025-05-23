load "data/cursos_online.csv";
filter column "modalidad" != "Híbrida" AND;
filter column "modalidad" == "Autodirigida";
aggregate COUNT column "estado_curso";
aggregate COUNT column "calificacion_final";
print;