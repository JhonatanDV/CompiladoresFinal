load "data/cursos_online.csv";
filter column "fecha_fin" < 2022-04-11 AND;
filter column "curso" != "Machine Learning" AND;
filter column "fecha_inicio" > 2023-05-21;
aggregate COUNT column "fecha_fin";
aggregate COUNT column "estado_curso";
print;