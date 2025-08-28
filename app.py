import streamlit as st

# # streamlit UI
st.title('Power Calculator')
st.write('Enter a number to calculate its square, cube and fifth power')


def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n ** 5

# # get user input
n = st.number_input('Enter an integer:', value=1, step=1)

square_result = square(n)
cube_result = cube(n)
fifth_result = fifth_power(n)



# # get user input
# n = st.number_input('Enter an integer:', value=1, step=1)

# # calculates the results
# square = n ** 2
# cube = n ** 3
# fifth_power = n ** 5

# # display results
# st.write(f'The square of {n}', {square})
# st.write(f'The cube of {n} is ', {cube})
# st.write(f'The fifth power of {n} is', {fifth_power})

# display results
st.write(f'The square of ', {square_result})
st.write(f'The cube of  is ', {cube_result})
st.write(f'The fifth power of  is', {fifth_result})