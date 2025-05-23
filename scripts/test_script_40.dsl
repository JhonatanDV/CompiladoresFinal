load "data/cursos_online.csv";
filter column "porcentaje_avance" == 7;
aggregate AVERAGE column "porcentaje_avance";
aggregate COUNT column "id_estudiante";
print;