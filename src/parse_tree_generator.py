"""
Parse Tree Generator for CSV Query DSL
Generates visual parse trees in PNG format
"""

import os
import re
from graphviz import Digraph

class ParseTreeNode:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

class ParseTreeGenerator:
    def __init__(self):
        self.node_counter = 0
        
    def generate_parse_tree(self, dsl_content, output_file="doc/parse_tree.png"):
        """Generate a parse tree from DSL content"""
        
        # Create the root node
        root = ParseTreeNode("program")
        
        # Parse statements
        statements = self._parse_statements(dsl_content)
        
        for stmt in statements:
            stmt_node = self._parse_statement(stmt)
            if stmt_node:
                root.add_child(stmt_node)
        
        # Generate the visual tree
        self._generate_visual_tree(root, output_file)
        return output_file
    
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
    
    def _parse_statement(self, statement):
        """Parse a single statement into a tree node"""
        statement = statement.strip()
        
        if statement.startswith('load '):
            return self._parse_load_statement(statement)
        elif statement.startswith('filter '):
            return self._parse_filter_statement(statement)
        elif statement.startswith('aggregate '):
            return self._parse_aggregate_statement(statement)
        elif statement == 'print':
            return self._parse_print_statement()
        
        return None
    
    def _parse_load_statement(self, statement):
        """Parse load statement"""
        node = ParseTreeNode("loadStatement")
        
        # Add LOAD token
        load_node = ParseTreeNode("LOAD", "load")
        node.add_child(load_node)
        
        # Extract filename
        match = re.match(r'load\s+"([^"]+)"', statement)
        if match:
            filename = match.group(1)
            string_node = ParseTreeNode("STRING", f'"{filename}"')
            node.add_child(string_node)
        
        # Add semicolon
        semicolon_node = ParseTreeNode("SEMICOLON", ";")
        node.add_child(semicolon_node)
        
        return node
    
    def _parse_filter_statement(self, statement):
        """Parse filter statement"""
        node = ParseTreeNode("filterStatement")
        
        # Add FILTER token
        filter_node = ParseTreeNode("FILTER", "filter")
        node.add_child(filter_node)
        
        # Add COLUMN token
        column_node = ParseTreeNode("COLUMN", "column")
        node.add_child(column_node)
        
        # Handle logical operators
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
            column_name = match.group(1)
            operator = match.group(2)
            value_str = match.group(3).strip()
            
            # Add column name
            string_node = ParseTreeNode("STRING", f'"{column_name}"')
            node.add_child(string_node)
            
            # Add operator
            op_node = ParseTreeNode("operator")
            op_token = ParseTreeNode(self._get_operator_token(operator), operator)
            op_node.add_child(op_token)
            node.add_child(op_node)
            
            # Add value
            value_node = ParseTreeNode("value")
            value_token = self._parse_value_node(value_str)
            value_node.add_child(value_token)
            node.add_child(value_node)
            
            # Add logical operator if present
            if logical_op:
                logical_node = ParseTreeNode("logicalOp")
                logical_token = ParseTreeNode(logical_op, logical_op)
                logical_node.add_child(logical_token)
                node.add_child(logical_node)
        
        return node
    
    def _parse_aggregate_statement(self, statement):
        """Parse aggregate statement"""
        node = ParseTreeNode("aggregateStatement")
        
        # Add AGGREGATE token
        agg_node = ParseTreeNode("AGGREGATE", "aggregate")
        node.add_child(agg_node)
        
        # Parse pattern
        pattern = r'aggregate\s+(COUNT|SUM|AVERAGE|BETWEEN)\s+column\s+"([^"]+)"'
        match = re.match(pattern, statement)
        
        if match:
            function = match.group(1)
            column = match.group(2)
            
            # Add aggregate function
            func_node = ParseTreeNode("aggregateFunction")
            func_token = ParseTreeNode(function, function)
            func_node.add_child(func_token)
            node.add_child(func_node)
            
            # Add COLUMN token
            column_token = ParseTreeNode("COLUMN", "column")
            node.add_child(column_token)
            
            # Add column name
            string_node = ParseTreeNode("STRING", f'"{column}"')
            node.add_child(string_node)
        
        # Add semicolon
        semicolon_node = ParseTreeNode("SEMICOLON", ";")
        node.add_child(semicolon_node)
        
        return node
    
    def _parse_print_statement(self):
        """Parse print statement"""
        node = ParseTreeNode("printStatement")
        
        # Add PRINT token
        print_node = ParseTreeNode("PRINT", "print")
        node.add_child(print_node)
        
        # Add semicolon
        semicolon_node = ParseTreeNode("SEMICOLON", ";")
        node.add_child(semicolon_node)
        
        return node
    
    def _get_operator_token(self, operator):
        """Get the token name for an operator"""
        token_map = {
            '>=': 'GTE',
            '<=': 'LTE',
            '>': 'GT',
            '<': 'LT',
            '==': 'EQ',
            '!=': 'NEQ'
        }
        return token_map.get(operator, 'OPERATOR')
    
    def _parse_value_node(self, value_str):
        """Parse a value into appropriate token"""
        value_str = value_str.strip()
        
        # String value (quoted)
        if value_str.startswith('"') and value_str.endswith('"'):
            return ParseTreeNode("STRING", value_str)
        
        # Date value (YYYY-MM-DD format)
        if re.match(r'\d{4}-\d{2}-\d{2}', value_str):
            return ParseTreeNode("DATE", value_str)
        
        # Numeric value
        try:
            if '.' in value_str:
                float(value_str)
                return ParseTreeNode("NUMBER", value_str)
            else:
                int(value_str)
                return ParseTreeNode("NUMBER", value_str)
        except ValueError:
            pass
        
        # Default to string
        return ParseTreeNode("STRING", f'"{value_str}"')
    
    def _generate_visual_tree(self, root, output_file):
        """Generate visual tree using Graphviz"""
        try:
            dot = Digraph(comment='Parse Tree', format='png')
            dot.attr(rankdir='TD')
            dot.attr('node', shape='ellipse', style='filled', fillcolor='lightblue')
            
            self._add_nodes_to_graph(dot, root, None)
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Render the graph
            dot.render(output_file.replace('.png', ''), cleanup=True)
            print(f"✓ Parse tree generated: {output_file}")
            
        except ImportError:
            print("Warning: Graphviz not available. Generating text-based tree instead.")
            self._generate_text_tree(root, output_file.replace('.png', '.txt'))
    
    def _add_nodes_to_graph(self, dot, node, parent_id):
        """Recursively add nodes to the graph"""
        node_id = f"node_{self.node_counter}"
        self.node_counter += 1
        
        # Create label for the node
        if node.value:
            label = f"{node.label}\\n'{node.value}'"
        else:
            label = node.label
        
        # Set different colors for different node types
        if node.value:  # Terminal nodes
            dot.node(node_id, label, fillcolor='lightgreen')
        else:  # Non-terminal nodes
            dot.node(node_id, label, fillcolor='lightblue')
        
        # Add edge from parent
        if parent_id:
            dot.edge(parent_id, node_id)
        
        # Add children
        for child in node.children:
            self._add_nodes_to_graph(dot, child, node_id)
    
    def _generate_text_tree(self, root, output_file):
        """Generate text-based tree as fallback"""
        with open(output_file, 'w') as f:
            f.write("Parse Tree (Text Format)\n")
            f.write("="*30 + "\n\n")
            self._write_text_tree(f, root, 0)
        
        print(f"✓ Text-based parse tree generated: {output_file}")
    
    def _write_text_tree(self, f, node, depth):
        """Write text tree recursively"""
        indent = "  " * depth
        if node.value:
            f.write(f"{indent}{node.label}: '{node.value}'\n")
        else:
            f.write(f"{indent}{node.label}\n")
        
        for child in node.children:
            self._write_text_tree(f, child, depth + 1)

def generate_parse_tree_for_script(script_file, output_file=None):
    """Generate parse tree for a specific script file"""
    if output_file is None:
        base_name = os.path.splitext(os.path.basename(script_file))[0]
        output_file = f"doc/{base_name}_parse_tree.png"
    
    try:
        with open(script_file, 'r') as f:
            content = f.read()
        
        generator = ParseTreeGenerator()
        return generator.generate_parse_tree(content, output_file)
        
    except Exception as e:
        print(f"Error generating parse tree for {script_file}: {e}")
        return None

if __name__ == "__main__":
    # Generate parse tree for demo script
    generate_parse_tree_for_script("scripts/demo_parse_tree.dsl", "doc/demo_parse_tree.png")