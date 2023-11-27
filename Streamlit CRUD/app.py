import streamlit as st
import mysql.connector

# Establish a connection to MySQL Server

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9803474343",
    database="crud_new1"
)