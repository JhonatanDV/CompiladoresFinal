import os
import random

def generate_test_scripts(num_scripts=40, output_dir='scripts'):
    """Generate 40 different DSL test scripts"""
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Define possible filter combinations
    columns = ['id_estudiante', 'curso', 'porcentaje_avance', 'calificacion_final', 
               'fecha_inicio', 'fecha_fin', 'estado_curso', 'modalidad', 'plataforma']
    
    numeric_columns = ['porcentaje_avance', 'calificacion_final']
    string_columns = ['id_estudiante', 'curso', 'estado_curso', 'modalidad', 'plataforma']
    date_columns = ['fecha_inicio', 'fecha_fin']
    
    operators = ['>=', '<=', '>', '<', '==', '!=']
    numeric_operators = ['>=', '<=', '>', '<', '==', '!=']
    string_operators = ['==', '!=']
    
    aggregations = ['COUNT', 'SUM', 'AVERAGE']
    logical_ops = ['AND', 'OR']
    
    # Predefined values for realistic filtering
    estados = ['Activo', 'Completado', 'Pausado', 'Cancelado', 'En Progreso']
    modalidades = ['Virtual', 'Presencial', 'Híbrida', 'Autodirigida']
    plataformas = ['Coursera', 'Udemy', 'edX', 'Platzi', 'Khan Academy', 
                   'LinkedIn Learning', 'Skillshare', 'MasterClass', 
                   'Codecademy', 'FreeCodeCamp']
    
    scripts = []
    
    for i in range(num_scripts):
        script_lines = []
        script_name = f"test_script_{i+1:02d}.dsl"
        
        # Always start with load
        script_lines.append('load "data/cursos_online.csv";')
        
        # Add 1-3 filters
        num_filters = random.randint(1, 3)
        
        for j in range(num_filters):
            # Choose column and appropriate operator/value
            if j == 0:
                # First filter - no logical operator
                filter_line = generate_filter_line(
                    columns, numeric_columns, string_columns, date_columns,
                    numeric_operators, string_operators, estados, modalidades, plataformas
                )
            else:
                # Subsequent filters - add logical operator to previous line
                logical_op = random.choice(logical_ops)
                # Fix the previous filter line to include logical operator
                prev_line = script_lines[-1].rstrip(';')
                script_lines[-1] = prev_line + f' {logical_op};'
                
                filter_line = generate_filter_line(
                    columns, numeric_columns, string_columns, date_columns,
                    numeric_operators, string_operators, estados, modalidades, plataformas
                )
            
            script_lines.append(filter_line)
        
        # Add 1-2 aggregations
        num_aggregations = random.randint(1, 2)
        used_columns = set()
        
        for _ in range(num_aggregations):
            agg_function = random.choice(aggregations)
            
            # Choose appropriate column for aggregation
            if agg_function in ['SUM', 'AVERAGE']:
                available_cols = [col for col in numeric_columns if col not in used_columns]
                if not available_cols:
                    available_cols = numeric_columns
            else:  # COUNT
                available_cols = [col for col in columns if col not in used_columns]
                if not available_cols:
                    available_cols = columns
            
            agg_column = random.choice(available_cols)
            used_columns.add(agg_column)
            
            script_lines.append(f'aggregate {agg_function} column "{agg_column}";')
        
        # End with print
        script_lines.append('print;')
        
        scripts.append({
            'name': script_name,
            'content': '\n'.join(script_lines)
        })
    
    # Write scripts to files
    for script in scripts:
        filepath = os.path.join(output_dir, script['name'])
        with open(filepath, 'w') as f:
            f.write(script['content'])
    
    print(f"Generated {len(scripts)} test scripts in {output_dir}/")
    
    # Create a special script for parse tree demonstration
    demo_script = '''load "data/cursos_online.csv";
filter column "estado_curso" == "Completado" AND;
filter column "porcentaje_avance" >= 90;
aggregate COUNT column "id_estudiante";
aggregate AVERAGE column "calificacion_final";
print;'''
    
    with open(os.path.join(output_dir, 'demo_parse_tree.dsl'), 'w') as f:
        f.write(demo_script)
    
    print("Created demo_parse_tree.dsl for parse tree demonstration")
    
    return scripts

def generate_filter_line(columns, numeric_columns, string_columns, date_columns,
                        numeric_operators, string_operators, estados, modalidades, plataformas):
    """Generate a single filter line"""
    
    column = random.choice(columns)
    
    if column in numeric_columns:
        operator = random.choice(numeric_operators)
        if column == 'porcentaje_avance':
            value = random.randint(0, 100)
        else:  # calificacion_final
            value = round(random.uniform(0, 100), 1)
        return f'filter column "{column}" {operator} {value};'
    
    elif column in string_columns:
        operator = random.choice(string_operators)
        if column == 'estado_curso':
            value = random.choice(estados)
        elif column == 'modalidad':
            value = random.choice(modalidades)
        elif column == 'plataforma':
            value = random.choice(plataformas)
        else:  # id_estudiante, curso
            if column == 'id_estudiante':
                value = f'EST{random.randint(1, 1000):04d}'
            else:  # curso
                cursos = ['Python Básico', 'JavaScript Avanzado', 'Data Science con R',
                         'Machine Learning', 'Desarrollo Web Full Stack']
                value = random.choice(cursos)
        return f'filter column "{column}" {operator} "{value}";'
    
    elif column in date_columns:
        operator = random.choice(['>=', '<=', '>', '<', '=='])
        # Generate a date in the last 2 years
        year = random.choice([2022, 2023, 2024])
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date_value = f'{year}-{month:02d}-{day:02d}'
        return f'filter column "{column}" {operator} {date_value};'
    
    else:
        # Fallback
        return f'filter column "{column}" == "test";'

if __name__ == "__main__":
    generate_test_scripts(40, 'scripts')
