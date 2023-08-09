def print_operation_table(operation, num_rows=6, num_columns=6):
    table = "|   |"
    for j in range(1, num_columns+1):
        table += f" {j} |"
    table += "\n|---|" + "---|" * num_columns + "\n"

    for i in range(1, num_rows+1):
        table += f"| {i} |"
        for j in range(1, num_columns+1):
            table += f" {operation(i, j)} |"
        table += "\n"

    print(table)

print_operation_table(lambda x, y: x * y)