# CSV Query DSL - Design Documentation

## 1. Overview

The CSV Query DSL (Domain Specific Language) is designed to provide a simple, intuitive interface for querying CSV data files. The language follows a command-based approach with deferred execution, allowing users to build complex queries that execute efficiently.

## 2. Design Principles

### 2.1 Simplicity
- Command-based syntax that reads like natural language
- Minimal set of keywords and operators
- Clear separation between data loading, filtering, aggregation, and output

### 2.2 Deferred Execution
- Operations accumulate without immediate execution
- All operations execute simultaneously when `print` is invoked
- Enables query optimization and batch processing

### 2.3 Flexibility
- Support for multiple filter conditions with logical operators
- Various aggregation functions for different data types
- Extensible design for adding new operations

### 2.4 Type Safety
- Appropriate operators for different data types
- Runtime validation of column names and operations
- Clear error messages for invalid operations

## 3. Language Grammar

### 3.1 EBNF Grammar

```ebnf
program := statement* EOF

statement := loadStatement
           | filterStatement
           | aggregateStatement
           | printStatement

loadStatement := 'load' STRING ';'

filterStatement := 'filter' 'column' STRING operator value logicalOp?

aggregateStatement := 'aggregate' aggregateFunction 'column' STRING ';'

printStatement := 'print' ';'

operator := '>=' | '<=' | '>' | '<' | '==' | '!='

logicalOp := 'AND' | 'OR'

aggregateFunction := 'COUNT' | 'SUM' | 'AVERAGE' | 'BETWEEN'

value := STRING | NUMBER | DATE
