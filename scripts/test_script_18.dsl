load "data/cursos_online.csv";
filter column "curso" == "Machine Learning" OR;
filter column "fecha_inicio" <= 2022-06-27 AND;
filter column "estado_curso" == "Pausado";
aggregate SUM column "porcentaje_avance";
print;