function euler20()
    return sum([parse(Int64, a) for a in string(factorial(big"100"))])
end

print(euler20())