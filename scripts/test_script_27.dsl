load "data/cursos_online.csv";
filter column "modalidad" != "Presencial" OR;
filter column "id_estudiante" != "EST0245" AND;
filter column "fecha_fin" == 2022-04-11;
aggregate COUNT column "curso";
print;