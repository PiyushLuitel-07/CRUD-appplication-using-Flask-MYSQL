import streamlit as st
import mysql.connector

# Establish a connection to MySQL Server

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="9803474343",
    database="crud_new1"
)

mycursor=mydb.cursor()

#Create Streamlit Application

def main():
    st.title("Welcome to CRUD Application")
    # display options for CRUD operation
    option=st.sidebar.selectbox("Select an operation",("Create","Read","Update","Delete"))
    # Perform operation
    if option=="Create":
        st.subheader("Create new Record")
        name=st.text_input("Enter your name")
        email=st.text_input("Enter your E-mail")
        if st.button("Create"):
            sql="insert into users(name,email) values(%s,%s)"
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record Created Successfully!")


    elif option=="Read":
        st.subheader("Read Records")
        mycursor.execute("select * from users")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)



    elif option=="Update":
        st.subheader("Update Record")


    elif option=="Delete":
        st.subheader("Delete Record")


if __name__=="__main__":
    main()