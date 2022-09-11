@time begin

function euler1(n)
    total = 0
    for i in range(1, 999)
        if i % 3 == 0 || i % 5 == 0
            total += i
        end
    end
    return total
end

print(euler1(1000))
end
