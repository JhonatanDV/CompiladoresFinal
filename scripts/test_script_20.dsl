load "data/cursos_online.csv";
filter column "estado_curso" == "En Progreso" AND;
filter column "calificacion_final" > 92.1 OR;
filter column "estado_curso" == "Completado";
aggregate SUM column "calificacion_final";
aggregate COUNT column "fecha_inicio";
print;