## lambda arguments: expression
Key Characteristics

### Anonymous: 
No name is assigned to the function.
### Single Expression: 
Can only contain one expression, evaluated and returned.
### Inline: 
Often used inline within other functions or methods.
### No Statements: 
Cannot contain statements like return, pass, or loops.

#### Lambda functions in Python are small, anonymous functions defined with the lambda keyword. 
#### They can have any number of arguments but only one expression, which is evaluated and returned.


df['Sales_Category'] = df['Sales_Amount'].apply(

    lambda x: 'High' if x > 1000 else 'Medium' if x > 500 else 'Low'
)

Lambda Function Description

Syntax: lambda x: 'High' if x > 1000 else 'Medium' if x > 500 else 'Low'

lambda: Keyword to define an anonymous (unnamed) function.

x: The input parameter, representing each value in the Sales_Amount column.

:: Separates the input parameter from the expression.

Expression: 'High' if x > 1000 else 'Medium' if x > 500 else 'Low'

A nested conditional (ternary) expression that evaluates x and returns a string.

Logic:

If x > 1000, return 'High'.

Else, if x > 500, return 'Medium'.

Else, return 'Low'.



Context:

The lambda function is passed to df['Sales_Amount'].apply(), which applies it to each element in the Sales_Amount column.

The result is stored in a new column, Sales_Category, in the DataFrame df.


Purpose:

Categorizes numerical sales amounts into discrete categories for easier analysis or visualization.

Concise alternative to defining a separate function or using multiple if statements.


How It Works:

For each value x in Sales_Amount:

If x = 1200, 1200 > 1000, so 'High' is assigned.

If x = 800, 800 ≤ 1000 but 800 > 500, so 'Medium' is assigned.

If x = 300, 300 ≤ 1000 and 300 ≤ 500, so 'Low' is assigned.
