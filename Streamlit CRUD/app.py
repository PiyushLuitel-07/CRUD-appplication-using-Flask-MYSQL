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
    st.sidebar.title("CRUD App")
    option=st.sidebar.selectbox("Select an operation",("Create","Read","Update","Delete"))
    # Perform operation
    if option=="Create":
        st.sidebar.subheader("Creates a new record with attributes in the database")
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
        st.sidebar.subheader("Displays all the records present in database")
        st.subheader("Read Records")
        if st.button("Read"):
            mycursor.execute("select * from users")
            result=mycursor.fetchall()
            for row in result:
                st.write(row)



    elif option=="Update":
            st.sidebar.subheader("Update attributes when needed")
            st.subheader("Update Record")
        
            choice=st.selectbox("Attribute that you want to update",("Name","E-mail","Name and E-mail"))

            if choice=="Name and E-mail":
                id=st.number_input("Enter ID of the data to be updated",min_value=1)
                name=st.text_input("Enter new name")
                email=st.text_input("Enter new E-mail")
                if st.button("Update"):
                    sql="update users set name=%s, email=%s where id=%s"
                    val=(name,email,id)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    st.success("Record updated successfully!")

            elif choice=="Name":
                id=st.number_input("Enter ID of the data to be updated",min_value=1)
                name=st.text_input("Enter new name")
                if st.button("Update"):
                    sql="update users set name=%s where id=%s"
                    val=(name,id)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    st.success("Record updated successfully!")
            
            elif choice=="E-mail":
                id=st.number_input("Enter ID of the data to be updated",min_value=1)
                email=st.text_input("Enter new E-mail")
                if st.button("Update"):
                    sql="update users set email=%s where id=%s"
                    val=(email,id)
                    mycursor.execute(sql,val)
                    mydb.commit()
                    st.success("Record updated successfully!")

            


    elif option=="Delete":
        st.sidebar.subheader("Delete a row from the database")
        st.subheader("Delete Record")
        id=st.number_input("Enter ID of data to be deleted",min_value=1)
        if st.button("Delete"):
            sql="delete from users where id=%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record deleted successfully !! ")

if __name__=="__main__":
    main()