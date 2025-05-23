#!/usr/bin/env python3
"""
Test runner for the CSV Query DSL
"""

import os
import sys
import time
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def run_comprehensive_tests():
    """Run comprehensive tests of the DSL"""
    
    print("CSV Query DSL - Comprehensive Test Suite")
    print("=" * 50)
    
    # Import after adding to path
    try:
        from src.query_processor import QueryProcessor
        from src.csv_query_interpreter import parse_dsl_string, CSVQueryDSLInterpreter
    except ImportError as e:
        print(f"Import error: {e}")
        print("Please run 'python main.py setup' first")
        return False
    
    # Check if data file exists
    if not os.path.exists("data/cursos_online.csv"):
        print("Data file not found. Generating...")
        try:
            from data.generate_csv import generate_courses_csv
            os.makedirs("data", exist_ok=True)
            generate_courses_csv("data/cursos_online.csv", 300)
        except Exception as e:
            print(f"Failed to generate data: {e}")
            return False
    
    # Test 1: Basic functionality test
    print("\n1. Testing basic DSL functionality...")
    interpreter = CSVQueryDSLInterpreter()
    
    basic_script = '''load "data/cursos_online.csv";
filter column "estado_curso" == "Completado";
aggregate COUNT column "id_estudiante";
print;'''
    
    try:
        tree = parse_dsl_string(basic_script, interpreter)
        if tree:
            print("✓ Basic functionality test passed")
        else:
            print("✗ Basic functionality test failed")
            return False
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        return False
    
    # Test 2: Complex filters test
    print("\n2. Testing complex filters...")
    interpreter.reset()
    
    complex_script = '''load "data/cursos_online.csv";
filter column "porcentaje_avance" >= 80 AND;
filter column "calificacion_final" > 70;
aggregate AVERAGE column "calificacion_final";
aggregate COUNT column "id_estudiante";
print;'''
    
    try:
        tree = parse_dsl_string(complex_script, interpreter)
        if tree:
            print("✓ Complex filters test passed")
        else:
            print("✗ Complex filters test failed")
            return False
    except Exception as e:
        print(f"✗ Complex filters test failed: {e}")
        return False
    
    # Test 3: Multiple aggregations test
    print("\n3. Testing multiple aggregations...")
    interpreter.reset()
    
    aggregation_script = '''load "data/cursos_online.csv";
filter column "estado_curso" == "Completado";
aggregate COUNT column "id_estudiante";
aggregate AVERAGE column "porcentaje_avance";
aggregate SUM column "calificacion_final";
print;'''
    
    try:
        tree = parse_dsl_string(aggregation_script, interpreter)
        if tree:
            print("✓ Multiple aggregations test passed")
        else:
            print("✗ Multiple aggregations test failed")
            return False
    except Exception as e:
        print(f"✗ Multiple aggregations test failed: {e}")
        return False
    
    # Test 4: All generated scripts
    print("\n4. Testing all generated scripts...")
    
    processor = QueryProcessor()
    
    if os.path.exists("scripts"):
        start_time = time.time()
        success = processor.execute_all_scripts_in_directory("scripts")
        end_time = time.time()
        
        if success:
            print(f"✓ All scripts test passed in {end_time - start_time:.2f} seconds")
        else:
            print("✗ Some scripts failed")
            return False
    else:
        print("Scripts directory not found. Generating...")
        try:
            from scripts.generate_test_scripts import generate_test_scripts
            generate_test_scripts(40, "scripts")
            success = processor.execute_all_scripts_in_directory("scripts")
            if success:
                print("✓ Generated and executed all scripts successfully")
            else:
                print("✗ Some generated scripts failed")
                return False
        except Exception as e:
            print(f"✗ Failed to generate/run scripts: {e}")
            return False
    
    # Test 5: Error handling
    print("\n5. Testing error handling...")
    interpreter.reset()
    
    # Test with non-existent file
    error_script1 = '''load "nonexistent.csv";
print;'''
    
    try:
        parse_dsl_string(error_script1, interpreter)
        print("✓ Non-existent file error handling passed")
    except Exception as e:
        print(f"✗ Error handling test failed: {e}")
        return False
    
    # Test with invalid column
    interpreter.reset()
    error_script2 = '''load "data/cursos_online.csv";
filter column "invalid_column" == "test";
print;'''
    
    try:
        parse_dsl_string(error_script2, interpreter)
        print("✓ Invalid column error handling passed")
    except Exception as e:
        print(f"✗ Error handling test failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("ALL TESTS PASSED! ✓")
    print("=" * 50)
    
    return True

def run_performance_test():
    """Run performance tests"""
    print("\n6. Running performance test...")
    
    try:
        from src.query_processor import QueryProcessor
        import time
        
        processor = QueryProcessor()
        
        # Large dataset test
        large_script = '''load "data/cursos_online.csv";
filter column "porcentaje_avance" > 50 AND;
filter column "estado_curso" != "Cancelado";
aggregate COUNT column "id_estudiante";
aggregate AVERAGE column "calificacion_final";
aggregate SUM column "porcentaje_avance";
print;'''
        
        start_time = time.time()
        success = processor.execute_script_string(large_script, "performance_test")
        end_time = time.time()
        
        if success:
            print(f"✓ Performance test passed in {end_time - start_time:.4f} seconds")
        else:
            print("✗ Performance test failed")
            return False
            
    except Exception as e:
        print(f"✗ Performance test failed: {e}")
        return False
    
    return True

def main():
    """Main test runner"""
    print("Starting comprehensive DSL tests...")
    
    # Run main tests
    if not run_comprehensive_tests():
        sys.exit(1)
    
    # Run performance test
    if not run_performance_test():
        sys.exit(1)
    
    print("\nAll tests completed successfully! 🎉")

if __name__ == "__main__":
    main()
