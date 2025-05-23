load "data/cursos_online.csv";
filter column "plataforma" != "MasterClass" AND;
filter column "fecha_inicio" == 2022-09-26 OR;
filter column "id_estudiante" != "EST0992";
aggregate AVERAGE column "calificacion_final";
aggregate AVERAGE column "porcentaje_avance";
print;