# CSV Query DSL Compiler

A Domain Specific Language (DSL) compiler built with ANTLR4 and Python for performing dynamic queries on CSV data files. This project implements a complete compiler with lexer, parser, and interpreter for processing structured data queries with deferred execution.

## Features

- **Complete DSL Implementation**: Custom grammar with ANTLR4 for CSV data queries
- **Deferred Execution**: Operations accumulate and execute only when `print` is called
- **Flexible Filtering**: Support for multiple filter conditions with logical operators (AND, OR)
- **Aggregation Functions**: COUNT, SUM, AVERAGE, and BETWEEN operations
- **Dynamic Query Processing**: 40+ test scripts demonstrating language flexibility
- **Error Handling**: Comprehensive error handling for invalid queries and data

## Project Structure

