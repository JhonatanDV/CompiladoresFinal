load "data/cursos_online.csv";
filter column "porcentaje_avance" < 30 OR;
filter column "modalidad" == "Presencial" OR;
filter column "fecha_fin" == 2023-04-22;
aggregate COUNT column "fecha_fin";
print;