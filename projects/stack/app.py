from stack.stack import Stack

if __name__ == '__main__':
    st = Stack()
    print(st)
    print(st.is_empty())
    st.push(2)
    st.push(3)
    st.push(1)
    a = st.pop()
    print(a)
    print(st)
    print(st.is_empty())
    print(st.is_full())
