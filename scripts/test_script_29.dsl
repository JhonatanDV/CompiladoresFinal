load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0692" AND;
filter column "fecha_inicio" <= 2023-06-08;
aggregate COUNT column "modalidad";
print;