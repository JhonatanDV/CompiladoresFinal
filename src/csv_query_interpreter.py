import sys
import os
import pandas as pd
from datetime import datetime
import re

# Add the src directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Use the simplified interpreter
from simple_dsl_interpreter import SimpleDSLInterpreter, parse_dsl_file, parse_dsl_string

# Maintain compatibility with existing interface
CSVQueryDSLInterpreter = SimpleDSLInterpreter