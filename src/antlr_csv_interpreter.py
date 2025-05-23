"""
ANTLR4-based CSV Query DSL Interpreter
Uses authentic ANTLR4 generated files for parsing
"""

import sys
import os
from antlr4 import *
from antlr4.tree.Trees import Trees
import pandas as pd
from datetime import datetime
import re

# Add the generated parser files to the path
grammar_path = os.path.join(os.path.dirname(__file__), '..', 'grammar', 'grammar')
sys.path.insert(0, grammar_path)

try:
    from CSVQueryDSLLexer import CSVQueryDSLLexer
    from CSVQueryDSLParser import CSVQueryDSLParser
    from CSVQueryDSLListener import CSVQueryDSLListener
    from CSVQueryDSLVisitor import CSVQueryDSLVisitor
    print("✓ ANTLR4 generated files loaded successfully")
except ImportError as e:
    print(f"✗ ANTLR4 generated files not found: {e}")
    # Fallback to simple interpreter
    from simple_dsl_interpreter import SimpleDSLInterpreter as FallbackInterpreter
    print("✓ Using fallback interpreter")

class CSVQueryDSLInterpreter(CSVQueryDSLListener):
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Reset the interpreter state"""
        self.csv_file = None
        self.data = None
        self.filters = []
        self.aggregations = []
        self.current_filter = {}
        self.results = []
        
    def enterLoadStatement(self, ctx):
        """Handle load statement"""
        filename = ctx.STRING().getText().strip('"')
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
    
    def enterFilterStatement(self, ctx):
        """Handle filter statement"""
        if self.data is None:
            print("Error: No CSV file loaded")
            return
            
        column = ctx.STRING().getText().strip('"')
        operator = ctx.operator().getText()
        
        # Handle different value types
        value_ctx = ctx.value()
        if value_ctx.STRING():
            value = value_ctx.STRING().getText().strip('"')
        elif value_ctx.NUMBER():
            try:
                if '.' in value_ctx.NUMBER().getText():
                    value = float(value_ctx.NUMBER().getText())
                else:
                    value = int(value_ctx.NUMBER().getText())
            except ValueError:
                value = value_ctx.NUMBER().getText()
        elif value_ctx.DATE():
            value = value_ctx.DATE().getText()
        else:
            value = None
            
        logical_op = None
        if ctx.logicalOp():
            logical_op = ctx.logicalOp().getText()
            
        filter_condition = {
            'column': column,
            'operator': operator,
            'value': value,
            'logical_op': logical_op
        }
        
        self.filters.append(filter_condition)
        print(f"Added filter: {column} {operator} {value}" + 
              (f" {logical_op}" if logical_op else ""))
    
    def enterAggregateStatement(self, ctx):
        """Handle aggregate statement"""
        if self.data is None:
            print("Error: No CSV file loaded")
            return
            
        function = ctx.aggregateFunction().getText()
        column = ctx.STRING().getText().strip('"')
        
        aggregation = {
            'function': function,
            'column': column
        }
        
        self.aggregations.append(aggregation)
        print(f"Added aggregation: {function} on column {column}")
    
    def enterPrintStatement(self, ctx):
        """Handle print statement - execute all accumulated operations"""
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
    """Parse a DSL file and execute it using ANTLR4"""
    if interpreter is None:
        interpreter = CSVQueryDSLInterpreter()
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
        
        # Create ANTLR input stream
        input_stream = InputStream(content)
        
        # Create lexer
        lexer = CSVQueryDSLLexer(input_stream)
        
        # Create token stream
        stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = CSVQueryDSLParser(stream)
        
        # Parse the input
        tree = parser.program()
        
        # Walk the tree with our interpreter
        walker = ParseTreeWalker()
        walker.walk(interpreter, tree)
        
        return True
        
    except FileNotFoundError:
        print(f"Error: DSL file {filename} not found")
        return False
    except Exception as e:
        print(f"Error parsing DSL file {filename}: {str(e)}")
        return False

def parse_dsl_string(dsl_content, interpreter=None):
    """Parse a DSL string and execute it using ANTLR4"""
    if interpreter is None:
        interpreter = CSVQueryDSLInterpreter()
    
    try:
        # Create ANTLR input stream
        input_stream = InputStream(dsl_content)
        
        # Create lexer
        lexer = CSVQueryDSLLexer(input_stream)
        
        # Create token stream
        stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = CSVQueryDSLParser(stream)
        
        # Parse the input
        tree = parser.program()
        
        # Walk the tree with our interpreter
        walker = ParseTreeWalker()
        walker.walk(interpreter, tree)
        
        return tree
        
    except Exception as e:
        print(f"Error parsing DSL: {str(e)}")
        return None

def generate_parse_tree_gui(script_file):
    """Generate GUI parse tree using ANTLR4"""
    try:
        with open(script_file, 'r') as file:
            content = file.read()
        
        # Create ANTLR input stream
        input_stream = InputStream(content)
        
        # Create lexer
        lexer = CSVQueryDSLLexer(input_stream)
        
        # Create token stream
        stream = CommonTokenStream(lexer)
        
        # Create parser
        parser = CSVQueryDSLParser(stream)
        
        # Parse the input
        tree = parser.program()
        
        # Print tree structure
        print("Parse Tree Structure:")
        print(Trees.toStringTree(tree, None, parser))
        
        return tree
        
    except Exception as e:
        print(f"Error generating parse tree: {e}")
        return None