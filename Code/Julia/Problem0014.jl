function euler14()
    largest_chain = 0
    best_number = 0
    for n in range(2, 999999)
        chain_count = 0
        current_number = n
        while true
            if n % 2 == 0
                chain_count += 1
                n = n / 2
            
            elseif n == 1
                break
            
            else
                chain_count += 1
                n = 3*n + 1
            end

        if chain_count > largest_chain
            largest_chain = chain_count
            best_number = current_number
        end
        end
    end
    return best_number
end

print(euler14())