function euler16()
    return sum(parse(Int64, i) for i in string(BigInt(2)^1000))
end

print(euler16())