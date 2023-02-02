import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def calculate_profit() -> float:
    '''
    Функция для подсчет прибыли
    :return: результат подсчета прибыли
    '''
    query_sql = f'''
        SELECT UnitPrice
        ,Quantity
          FROM invoice_items
        '''
    result = 0
    for datas in execute_query(query_sql):
        result += datas[0] * datas[1]
    return round(result, 2)


print(calculate_profit())


def get_nonunique_customers_by_sql() -> str:
    '''
    Функция вывода повторяющихся имен
    :print: список из повторящихся имен и сколько раз они повторяются
    '''
    query_sql = f'''
        SELECT FirstName, COUNT(*)
          FROM customers
          GROUP BY FirstName;
    '''
    for names in execute_query(query_sql):
        if names[1] > 1:
            print(names[0], names[1])


get_nonunique_customers_by_sql()

