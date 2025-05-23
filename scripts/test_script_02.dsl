load "data/cursos_online.csv";
filter column "plataforma" != "Khan Academy" AND;
filter column "plataforma" == "MasterClass";
aggregate AVERAGE column "porcentaje_avance";
aggregate COUNT column "fecha_fin";
print;