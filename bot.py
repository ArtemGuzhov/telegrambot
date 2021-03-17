# -*- coding: utf-8 -*-
import mariadb
import sys
from openpyxl import Workbook
import codecs
import telebot
import os

API_TOKEN = '' # Token of BOT

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['excel_of_db'])
def excel_of_db(message):
    try:
        # conn = mariadb.connect(
         conn = mariadb.connect(
            user="admin",
            password="1qazxsw2",
            host="192.168.2.20",
            port=3306,
            database="cam_test"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cur = conn.cursor()
    
    cam_list = 'cam_list'

    wb = Workbook()

    SQL = 'SELECT * FROM cam_list'
    cur.execute(SQL)
    results = cur.fetchall()
    ws = wb.create_sheet(0)

    for row in results:
        ws.append(row)

    workbook_name = "camers_list"
    wb.save(workbook_name + ".xlsx")

    f = codecs.open('camers_list.xlsx','rb')
    bot.send_document(message.from_user.id, f)

    # file_excel = '~/camers_list.xlsx'
    # os.remove(file_excel)

    cur.close()

if __name__ == '__main__':
    bot.polling(none_stop=True)
