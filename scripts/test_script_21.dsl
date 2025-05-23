load "data/cursos_online.csv";
filter column "fecha_fin" >= 2024-09-07 OR;
filter column "estado_curso" == "En Progreso" AND;
filter column "curso" != "Python Básico";
aggregate COUNT column "calificacion_final";
aggregate AVERAGE column "porcentaje_avance";
print;