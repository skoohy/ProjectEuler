function euler92()
    counter_89 = 0

    for num in range(1, 9999999)
        current_number = num
        while true
            ss_digits = sum([parse(Int64, a)^2 for a in string(current_number)])
            if ss_digits == 89
                counter_89 += 1
                break
            elseif ss_digits == 1
                break
            end
            current_number = ss_digits
        end
    end
    return counter_89
end

print(euler92())