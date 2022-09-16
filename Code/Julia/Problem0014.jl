@time begin
function euler14()
    largest_chain = 0
    best_number = 0
    for n in range(2, 1000000)
        chain = [1] # All numbers end at one
        num = n
        while true
            if n % 2 == 0
                push!(chain, n)
                n = n / 2
            elseif n == 1
                break
            else 
                push!(chain, n)
                n = 3*n + 1
            end
        end
    
        if length(chain) > largest_chain
            largest_chain = length(chain)
            best_number = num
        end
    end

    return best_number
end
euler14()
end
print(euler14())