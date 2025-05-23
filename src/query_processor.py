import os
import sys
from csv_query_interpreter import CSVQueryDSLInterpreter, parse_dsl_file, parse_dsl_string

class QueryProcessor:
    """Main class for processing DSL queries"""
    
    def __init__(self):
        self.interpreter = CSVQueryDSLInterpreter()
    
    def execute_script_file(self, script_path):
        """Execute a DSL script from file"""
        print(f"\n{'='*50}")
        print(f"Executing script: {script_path}")
        print(f"{'='*50}")
        
        success = parse_dsl_file(script_path, self.interpreter)
        
        if not success:
            print(f"Failed to execute script: {script_path}")
        
        return success
    
    def execute_script_string(self, script_content, script_name="inline"):
        """Execute a DSL script from string"""
        print(f"\n{'='*50}")
        print(f"Executing script: {script_name}")
        print(f"{'='*50}")
        
        tree = parse_dsl_string(script_content, self.interpreter)
        
        if tree is None:
            print(f"Failed to execute script: {script_name}")
            return False
            
        return True
    
    def execute_all_scripts_in_directory(self, scripts_dir):
        """Execute all DSL scripts in a directory"""
        if not os.path.exists(scripts_dir):
            print(f"Scripts directory not found: {scripts_dir}")
            return False
        
        script_files = [f for f in os.listdir(scripts_dir) if f.endswith('.dsl')]
        script_files.sort()
        
        if not script_files:
            print(f"No .dsl files found in {scripts_dir}")
            return False
        
        print(f"Found {len(script_files)} script files")
        
        successful = 0
        failed = 0
        
        for script_file in script_files:
            script_path = os.path.join(scripts_dir, script_file)
            success = self.execute_script_file(script_path)
            
            if success:
                successful += 1
            else:
                failed += 1
        
        print(f"\n{'='*50}")
        print(f"EXECUTION SUMMARY")
        print(f"{'='*50}")
        print(f"Total scripts: {len(script_files)}")
        print(f"Successful: {successful}")
        print(f"Failed: {failed}")
        
        return failed == 0
    
    def reset_interpreter(self):
        """Reset the interpreter state"""
        self.interpreter.reset()

def main():
    """Main function for command line usage"""
    if len(sys.argv) < 2:
        print("Usage: python query_processor.py <script_file_or_directory>")
        sys.exit(1)
    
    path = sys.argv[1]
    processor = QueryProcessor()
    
    if os.path.isfile(path):
        # Single script file
        processor.execute_script_file(path)
    elif os.path.isdir(path):
        # Directory of scripts
        processor.execute_all_scripts_in_directory(path)
    else:
        print(f"Path not found: {path}")
        sys.exit(1)

if __name__ == "__main__":
    main()
