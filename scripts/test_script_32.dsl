load "data/cursos_online.csv";
filter column "fecha_inicio" == 2022-08-06 OR;
filter column "modalidad" != "Autodirigida" OR;
filter column "curso" != "Python Básico";
aggregate COUNT column "porcentaje_avance";
print;