@time begin
function euler1()
    total = 0
    for i in range(1, 999)
        if i % 3 == 0 || i % 5 == 0
            total += i
        end
    end
    return total
end
euler1()
end
print(euler1())
