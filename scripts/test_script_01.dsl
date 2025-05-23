load "data/cursos_online.csv";
filter column "estado_curso" == "En Progreso" OR;
filter column "estado_curso" != "En Progreso" OR;
filter column "curso" == "Data Science con R";
aggregate AVERAGE column "porcentaje_avance";
print;