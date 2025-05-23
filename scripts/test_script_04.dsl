load "data/cursos_online.csv";
filter column "porcentaje_avance" > 45 AND;
filter column "fecha_fin" < 2023-10-13 AND;
filter column "id_estudiante" != "EST0203";
aggregate COUNT column "fecha_fin";
aggregate AVERAGE column "calificacion_final";
print;