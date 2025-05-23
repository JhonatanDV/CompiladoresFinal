load "data/cursos_online.csv";
filter column "plataforma" != "Khan Academy" AND;
filter column "id_estudiante" == "EST0168" AND;
filter column "calificacion_final" == 68.2;
aggregate SUM column "porcentaje_avance";
print;