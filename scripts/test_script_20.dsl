load "data/cursos_online.csv";
filter column "id_estudiante" == "EST0934" OR;
filter column "modalidad" != "Virtual" OR;
filter column "plataforma" == "Codecademy";
aggregate SUM column "calificacion_final";
aggregate SUM column "porcentaje_avance";
print;