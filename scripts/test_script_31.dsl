load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0417" AND;
filter column "calificacion_final" == 11.0;
aggregate SUM column "porcentaje_avance";
aggregate COUNT column "estado_curso";
print;