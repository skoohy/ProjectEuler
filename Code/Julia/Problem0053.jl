@time begin
function euler53()
    count = 0
    for n in range(1, 100)
        for r in range(1, 100)
            if binomial(BigInt(n), BigInt(r)) > 1e6
                count += 1
            end
        end
    end
    return count
end
euler53()
end
print(euler53())
