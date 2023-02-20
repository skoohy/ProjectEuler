function euler53()
    count = 0

    for r in range(1, 100)
        r = BigInt(r)
        for n in range(r, 100)
            n = BigInt(n)
            if binomial(n,r) > 1e6
                count += 1
            end
        end
    end
    return count
end

print(euler53())