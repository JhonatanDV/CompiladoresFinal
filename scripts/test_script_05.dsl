load "data/cursos_online.csv";
filter column "modalidad" != "Presencial";
aggregate AVERAGE column "porcentaje_avance";
print;