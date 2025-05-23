"""
Simple DSL Interpreter for CSV Query Language
Implements a complete interpreter without complex ANTLR dependencies
"""

import re
import pandas as pd
import os
from datetime import datetime

class SimpleDSLInterpreter:
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset the interpreter state"""
        self.csv_file = None
        self.data = None
        self.filters = []
        self.aggregations = []
        self.results = []
    
    def parse_and_execute(self, dsl_content):
        """Parse and execute DSL content"""
        # Clean and split the content into statements
        statements = self._parse_statements(dsl_content)
        
        for statement in statements:
            self._execute_statement(statement)
    
    def _parse_statements(self, content):
        """Parse DSL content into individual statements"""
        # Remove comments
        content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        
        # Split by semicolons and clean
        statements = []
        for stmt in content.split(';'):
            stmt = stmt.strip()
            if stmt:
                statements.append(stmt)
        
        return statements
    
    def _execute_statement(self, statement):
        """Execute a single DSL statement"""
        statement = statement.strip()
        
        if statement.startswith('load '):
            self._execute_load(statement)
        elif statement.startswith('filter '):
            self._execute_filter(statement)
        elif statement.startswith('aggregate '):
            self._execute_aggregate(statement)
        elif statement == 'print':
            self._execute_print()
        else:
            print(f"Unknown statement: {statement}")
    
    def _execute_load(self, statement):
        """Execute load statement"""
        # Parse: load "filename.csv"
        match = re.match(r'load\s+"([^"]+)"', statement)
        if match:
            filename = match.group(1)
            self.csv_file = filename
            try:
                self.data = pd.read_csv(filename)
                print(f"Loaded CSV file: {filename} with {len(self.data)} records")
            except FileNotFoundError:
                print(f"Error: File {filename} not found")
                self.data = None
            except Exception as e:
                print(f"Error loading file {filename}: {str(e)}")
                self.data = None
        else:
            print(f"Invalid load statement: {statement}")
    
    def _execute_filter(self, statement):
        """Execute filter statement"""
        if self.data is None:
            print("Error: No CSV file loaded")
            return
        
        # Parse: filter column "column_name" operator value [AND/OR]
        # Handle trailing semicolon and logical operators properly
        statement = statement.strip()
        if statement.endswith(';'):
            statement = statement[:-1]
        
        # Extract logical operator if present at the end
        logical_op = None
        if statement.endswith(' AND'):
            logical_op = 'AND'
            statement = statement[:-4].strip()
        elif statement.endswith(' OR'):
            logical_op = 'OR'
            statement = statement[:-3].strip()
        
        # Parse the main filter pattern
        pattern = r'filter\s+column\s+"([^"]+)"\s+([><=!]+)\s+(.+)$'
        match = re.match(pattern, statement)
        
        if match:
            column = match.group(1)
            operator = match.group(2)
            value_str = match.group(3).strip()
            
            # Parse value (string, number, or date)
            value = self._parse_value(value_str)
            
            filter_condition = {
                'column': column,
                'operator': operator,
                'value': value,
                'logical_op': logical_op
            }
            
            self.filters.append(filter_condition)
            print(f"Added filter: {column} {operator} {value}" + 
                  (f" {logical_op}" if logical_op else ""))
        else:
            print(f"Invalid filter statement: {statement}")
    
    def _execute_aggregate(self, statement):
        """Execute aggregate statement"""
        if self.data is None:
            print("Error: No CSV file loaded")
            return
        
        # Parse: aggregate FUNCTION column "column_name"
        pattern = r'aggregate\s+(COUNT|SUM|AVERAGE|BETWEEN)\s+column\s+"([^"]+)"'
        match = re.match(pattern, statement)
        
        if match:
            function = match.group(1)
            column = match.group(2)
            
            aggregation = {
                'function': function,
                'column': column
            }
            
            self.aggregations.append(aggregation)
            print(f"Added aggregation: {function} on column {column}")
        else:
            print(f"Invalid aggregate statement: {statement}")
    
    def _execute_print(self):
        """Execute print statement - process all accumulated operations"""
        if self.data is None:
            print("Error: No CSV file loaded")
            return
        
        print("\n=== EXECUTING QUERY ===")
        
        # Apply filters
        filtered_data = self.data.copy()
        
        if self.filters:
            print("Applying filters...")
            filtered_data = self._apply_filters(filtered_data)
            print(f"Records after filtering: {len(filtered_data)}")
        
        # Apply aggregations
        if self.aggregations:
            print("Calculating aggregations...")
            for agg in self.aggregations:
                result = self._apply_aggregation(filtered_data, agg)
                self.results.append({
                    'type': 'aggregation',
                    'function': agg['function'],
                    'column': agg['column'],
                    'result': result
                })
                print(f"{agg['function']}({agg['column']}): {result}")
        
        # Show sample of filtered data if no aggregations
        if not self.aggregations and len(filtered_data) > 0:
            print("\nFirst 10 records:")
            print(filtered_data.head(10).to_string())
        elif not self.aggregations:
            print("No records match the filters")
        
        print("=== QUERY COMPLETED ===\n")
        
        # Reset for next query
        self.filters = []
        self.aggregations = []
    
    def _parse_value(self, value_str):
        """Parse a value string into appropriate type"""
        value_str = value_str.strip()
        
        # String value (quoted)
        if value_str.startswith('"') and value_str.endswith('"'):
            return value_str[1:-1]
        
        # Date value (YYYY-MM-DD format)
        if re.match(r'\d{4}-\d{2}-\d{2}', value_str):
            return value_str
        
        # Numeric value
        try:
            if '.' in value_str:
                return float(value_str)
            else:
                return int(value_str)
        except ValueError:
            pass
        
        # Default to string
        return value_str
    
    def _apply_filters(self, data):
        """Apply all accumulated filters to the data"""
        result = data.copy()
        
        for i, filter_cond in enumerate(self.filters):
            column = filter_cond['column']
            operator = filter_cond['operator']
            value = filter_cond['value']
            logical_op = filter_cond.get('logical_op')
            
            if column not in result.columns:
                print(f"Warning: Column '{column}' not found in data")
                continue
            
            # Create condition
            condition = self._create_condition(result[column], operator, value)
            
            if i == 0:
                # First filter
                result = result[condition]
            else:
                # Apply logical operator with previous result
                prev_logical_op = self.filters[i-1].get('logical_op', 'AND')
                if prev_logical_op == 'AND':
                    result = result[condition]
                elif prev_logical_op == 'OR':
                    # For OR, we need to combine with original data
                    or_condition = self._create_condition(data[column], operator, value)
                    or_result = data[or_condition]
                    result = pd.concat([result, or_result]).drop_duplicates()
        
        return result
    
    def _create_condition(self, series, operator, value):
        """Create a pandas condition based on operator and value"""
        try:
            if operator == '>=':
                return series >= value
            elif operator == '<=':
                return series <= value
            elif operator == '>':
                return series > value
            elif operator == '<':
                return series < value
            elif operator == '==':
                return series == value
            elif operator == '!=':
                return series != value
            else:
                print(f"Unknown operator: {operator}")
                return pd.Series([True] * len(series))
        except Exception as e:
            print(f"Error applying filter: {e}")
            return pd.Series([True] * len(series))
    
    def _apply_aggregation(self, data, aggregation):
        """Apply aggregation function to the data"""
        function = aggregation['function']
        column = aggregation['column']
        
        if column not in data.columns:
            print(f"Warning: Column '{column}' not found in data")
            return None
        
        try:
            if function == 'COUNT':
                return len(data[column].dropna())
            elif function == 'SUM':
                return data[column].sum()
            elif function == 'AVERAGE':
                return data[column].mean()
            elif function == 'BETWEEN':
                # For BETWEEN, we'll return min and max
                return f"{data[column].min()} - {data[column].max()}"
            else:
                print(f"Unknown aggregation function: {function}")
                return None
        except Exception as e:
            print(f"Error calculating {function} for column {column}: {e}")
            return None

def parse_dsl_file(filename, interpreter=None):
    """Parse a DSL file and execute it"""
    if interpreter is None:
        interpreter = SimpleDSLInterpreter()
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        interpreter.parse_and_execute(content)
        return True
        
    except FileNotFoundError:
        print(f"Error: DSL file {filename} not found")
        return False
    except Exception as e:
        print(f"Error parsing DSL file {filename}: {str(e)}")
        return False

def parse_dsl_string(dsl_content, interpreter=None):
    """Parse a DSL string and execute it"""
    if interpreter is None:
        interpreter = SimpleDSLInterpreter()
    
    try:
        interpreter.parse_and_execute(dsl_content)
        return True
    except Exception as e:
        print(f"Error parsing DSL: {str(e)}")
        return False