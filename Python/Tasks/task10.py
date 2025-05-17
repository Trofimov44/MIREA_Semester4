def main(input_table):
    unique_columns = []
    cols_to_keep = []
    num_cols = len(input_table[0]) if input_table else 0

    for col_idx in range(num_cols):
        current_col = [row[col_idx] for row in input_table]
        if current_col not in unique_columns:
            unique_columns.append(current_col)
            cols_to_keep.append(col_idx)

    table_step1 = []
    for row in input_table:
        new_row = [row[col_idx] for col_idx in cols_to_keep]
        table_step1.append(new_row)

    table_step2 = step1(table_step1)

    unique_rows = []
    table_step3 = []
    for row in table_step2:
        if row not in unique_rows:
            unique_rows.append(row)
            table_step3.append(row)

    table_step4 = step2(table_step3)
    table_step5 = sorted(table_step4, key=lambda x: x[0])

    result = step3(table_step5)

    return result


def step1(table_step1):
    if not table_step1:
        table_step2 = []
    else:
        non_empty_cols = []
        for col_idx in range(len(table_step1[0])):
            col_data = [row[col_idx] for row in table_step1]
            if any(cell is not None for cell in col_data):
                non_empty_cols.append(col_idx)

        table_step2 = []
        for row in table_step1:
            new_row = [row[col_idx] for col_idx in non_empty_cols]
            table_step2.append(new_row)
    return table_step2


def step2(table_step3):
    table_step4 = []
    for row in table_step3:
        name = None
        email = None
        flag = None
        phone = None

        for cell in row:
            if cell is None:
                continue

            if ',' in cell and '.' in cell:
                parts = cell.split(',')
                if len(parts) == 2:
                    last_name = parts[0].strip().replace('.', '')
                    initials = parts[1].strip().split('.')
                    if len(initials) >= 2:
                        name = f"{initials[0].strip()}. {last_name}"
            elif '@' in cell:
                email = cell.replace('@', '[at]')
            elif cell in ('0', '1'):
                flag = 'Да' if cell == '1' else 'Нет'
            elif '+' in cell:  # Телефон
                phone = cell.replace(' ', '').replace('-', '').replace('–', '')
                if phone.startswith('+7'):
                    phone = phone[2:]
                elif phone.startswith('7'):
                    phone = phone[1:]
                if len(phone) >= 10:
                    phone = f"{phone[:3]}-{phone[3:6]}-{phone[6:10]}"

        if all(v is not None for v in [name, email, flag, phone]):
            table_step4.append([name, email, flag, phone])
    return table_step4


def step3(table_step5):
    names = [row[0] for row in table_step5]
    emails = [row[1] for row in table_step5]
    flags = [row[2] for row in table_step5]
    phones = [row[3] for row in table_step5]

    return [names, emails, flags, phones]
