load "data/cursos_online.csv";
filter column "estado_curso" == "Cancelado";
aggregate AVERAGE column "porcentaje_avance";
aggregate AVERAGE column "calificacion_final";
print;