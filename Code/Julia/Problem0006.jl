@time begin
function euler6()
    sum_of_squares = 0; s = 0
    for i in range(1, 100)
        sum_of_squares += (i)^2
        s += i
    end
    return (s)^2 - sum_of_squares
end
euler6()
end
print(euler6())