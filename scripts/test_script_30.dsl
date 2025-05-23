load "data/cursos_online.csv";
filter column "estado_curso" != "Cancelado";
aggregate SUM column "calificacion_final";
print;