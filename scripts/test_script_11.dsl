load "data/cursos_online.csv";
filter column "curso" == "Desarrollo Web Full Stack" OR;
filter column "fecha_inicio" == 2024-05-27;
aggregate AVERAGE column "porcentaje_avance";
print;