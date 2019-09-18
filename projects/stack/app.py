from stack.stack import Stack


def brute_force(prices):
    nelements = len(prices)
    span = [0] * nelements
    for i in range(nelements):
        span[i] = 1
        for j in range(i - 1, 0, -1):
            if prices[j] <= prices[i]:
                span[i] += 1
            else:
                break
    return span


def stack_span(prices):
    st = Stack()
    nelements = len(prices)
    span = [0] * nelements
    for i in range(nelements):
        while not (st.is_empty()) and prices[st.top()] <= prices[i]:
            _ = st.pop()
        span[i] = i + 1 if st.is_empty() else i - st.top()
        st.push(i)
    return span


if __name__ == '__main__':
    prices_ = [100, 80, 60, 70, 60, 75, 85]
    print(stack_span(prices_))
