load "data/cursos_online.csv";
filter column "estado_curso" != "Activo";
aggregate COUNT column "modalidad";
print;