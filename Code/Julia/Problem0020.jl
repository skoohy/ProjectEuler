@time begin
function euler20()
    return sum([parse(Int64, a) for a in string(factorial(big"100"))])
end
euler20()
end
print(euler20())