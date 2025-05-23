load "data/cursos_online.csv";
filter column "modalidad" == "Presencial" OR;
filter column "curso" == "Python Básico";
aggregate SUM column "calificacion_final";
print;