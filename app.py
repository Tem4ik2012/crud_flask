import sqlite3
from flask import Flask, render_template, request, redirect, url_for

# Создание БД
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Создаем таблицу
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,           
    last_name TEXT NOT NULL,           
    gender INTEGER NOT NULL,           
    age INTEGER NOT NULL,           
    phone TEXT NOT NULL,           
    email TEXT NOT NULL,           
    addres TEXT NOT NULL,           
    salary REAL NOT NULL           
    )
""")

conn.commit()
conn.close()