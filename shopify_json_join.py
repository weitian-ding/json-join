import json


def json_inner_join(rows1, rows2, key1, key2):

    """Computes the inner join of 2 json lists
    The Runtime is O(n^2), where n is max(len(rows1), lens(rows2)),
    assuming the number of fields in each json object is bounded by a constant

    Args:
        rows1 (list of dict): the first json list
        rows2 (list of dict): the second json list
        key1 (str): the key used in join in the first json list, must be integer type
        key2 (str): the key used in join in the second json list, must be integer type

    Returns:
        list of dict: the joined list
    """

    rows1_sorted = sorted(rows1, key=lambda row: row[key1])  # runtime O(nlogn)
    rows2_sorted = sorted(rows2, key=lambda row: row[key2])  # runtime O(nlogn)

    rows2_pos = 0

    result = []

    # join the 2 sorted list
    for row1 in rows1_sorted:  # Runtime O(n^2)

        while rows2_pos < len(rows2_sorted) and rows2_sorted[rows2_pos][key2] == row1[key1]:
            # join two rows
            joined = {}

            for key, value in row1.items():
                joined[key] = value

            for key, value in rows2_sorted[rows2_pos].items():
                joined[key] = value

            result.append(joined)

            rows2_pos += 1

        if rows2_pos >= len(rows2_sorted):
            break

    return result


def main():
    with open('customers.json') as json_file:
        customers = json.load(json_file)

    with open('orders.json') as json_file:
        orders = json.load(json_file)

    inner_joined = json_inner_join(customers, orders, 'cid', 'customer_id')

    # compute the order total for Barry and Steve

    total_for_barry = 0
    total_for_steve = 0

    for transaction in inner_joined:
        if transaction['name'] == 'Steve':
            total_for_steve += transaction['price']
        elif transaction['name'] == 'Barry':
            total_for_barry += transaction['price']

    print('length is {0}, total for Barry is ${1}, total for Steve is ${2}'.format(len(inner_joined),
          total_for_barry, total_for_steve))



if __name__ == '__main__':
    main()