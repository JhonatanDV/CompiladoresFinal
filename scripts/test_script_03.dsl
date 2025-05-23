load "data/cursos_online.csv";
filter column "fecha_inicio" == 2024-05-23;
aggregate COUNT column "modalidad";
print;