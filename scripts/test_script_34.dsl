load "data/cursos_online.csv";
filter column "fecha_fin" >= 2023-02-26 AND;
filter column "estado_curso" != "Pausado" AND;
filter column "id_estudiante" == "EST0068";
aggregate COUNT column "estado_curso";
print;