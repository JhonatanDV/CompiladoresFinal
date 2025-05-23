load "data/cursos_online.csv";
filter column "modalidad" != "Autodirigida";
aggregate COUNT column "id_estudiante";
aggregate COUNT column "curso";
print;