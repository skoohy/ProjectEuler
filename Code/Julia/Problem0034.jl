function euler34()
    ans = 0
    for n in range(1, 100000)
        if n != 1
            if n != 2
                if sum([factorial(parse(Int64, i)) for i in string(n)]) == n
                    ans += sum([factorial(parse(Int64, i)) for i in string(BigInt(n))])
                end
            end
        end
    end
    return ans
end

print(euler34())