load "data/cursos_online.csv";
filter column "estado_curso" == "Completado" AND;
filter column "porcentaje_avance" >= 90;
aggregate COUNT column "id_estudiante";
aggregate AVERAGE column "calificacion_final";
print;