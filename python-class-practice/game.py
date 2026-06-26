import random

# choice = ["paper","rock","scissors"]
# random_choice =random.choice(choice)

# user=input("Enter your choice: ")
# print("random_choice: ",random_choice)

# if user == random_choice:
#     print("TIE")
# elif user== "rock" and random_choice == "scissors" or user == "paper" and random_choice == "rock" or user == "scissors" and random_choice == "paper":
#      print("You Win")
# else:
#      print("computer win")
     


# choice = ["rock", "paper", "scissors"]
# user_score = 0
# computer_score = 0

# for i in range(3):
#     user = input("Enter choice: ")
#     computer = random.choice(choice)
#     print("Computer:", computer)

#     if user == computer:
#         print("Tie")
#     elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
#         print("You Win")
#         user_score += 1
#     else:
#         print("Computer Win")
#         computer_score += 1
#     if user_score > computer_score:
#         print("You Win")
#     elif computer_score > user_score:
#         print("Computer Win")


import streamlit as st

st.set_page_config(page_title="Number addition",page_icon="➕",layout="centered")
st.title("Addition of Two Numbers")
st.caption("Enter Two number and it will return addition of them")

form=st.form("add_form")
num1=form.number_input("First Number")
num2=form.number_input("Second Number")
submitted=form.form_submit_button("Calculate Sum")

if submitted:
    result=num1+num1
    st.divider()
    st.success(F"Sum{result}")
    st.metric(label="Result",value=result)

for i in range(1,11):
    st.write(2,"x",i,"=",2*i)




# choices = ["rock", "paper", "scissors"]

# st.title("🎮 Rock Paper Scissors")

# user = st.selectbox("Choose your move", choices)

# if st.button("Play"):
#     computer = random.choice(choices)

#     st.write(f"### Computer chose: {computer}")

#     if user == computer:
#         st.success("🤝 It's a Tie!")
#     elif user == "rock" and computer == "scissors" or user == "paper" and computer == "rock" or user == "scissors" and computer == "paper":
#         st.success("🎉 You Win!")
#     else:
#         st.error("💻 Computer Wins!")

