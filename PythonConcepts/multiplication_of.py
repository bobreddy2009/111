def multiplication_of(x):
    def multiplier(y):
        m_table1 = [x * i for i in range(13)]
        m_table2 = [y * i for i in range(13)]
        return m_table1, m_table2

    return multiplier
first_multiplier = multiplication_of(7)
print(first_multiplier(9)[0])
print(first_multiplier(9)[1])

