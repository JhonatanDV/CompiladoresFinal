load "data/cursos_online.csv";
filter column "calificacion_final" != 68.8;
aggregate COUNT column "id_estudiante";
aggregate AVERAGE column "porcentaje_avance";
print;