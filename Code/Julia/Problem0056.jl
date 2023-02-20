function euler56()
    max_sum = 0

    for a in range(1, 99)
        for b in range(1, 99)
            digit_sum = sum([parse(Int64, a) for a in string(BigInt(a)^b)])
            if digit_sum > max_sum
                max_sum = digit_sum
            end
        end
    end
    return max_sum
end

print(euler56())