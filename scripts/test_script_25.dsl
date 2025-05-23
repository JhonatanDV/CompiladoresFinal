load "data/cursos_online.csv";
filter column "modalidad" == "Virtual" AND;
filter column "curso" != "Data Science con R";
aggregate SUM column "porcentaje_avance";
aggregate COUNT column "curso";
print;