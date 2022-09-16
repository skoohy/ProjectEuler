@time begin
function euler56() 
    digits_sums = []
    for a in range(1, 99)
        for b in range(1, 99)
            
            digits = [parse(Int64, i) for i in string(BigInt(a)^b)]
            push!(digits_sums, sum(digits))
            #println(digits_sums)
        end
    end
    return maximum(digits_sums)
end
euler56()
end
print(euler56())
