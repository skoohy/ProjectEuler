function euler29()
    return length(Set([BigInt(a)^b for a in range(2,100) for b in range(2,100)]))
end

print(euler29())