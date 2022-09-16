@time begin
function euler92()
    cnt_89 = 0
    for num in range(1, 10000000)
        current_number = num
        while true
            ss_digits = sum([parse(Int64, a) for a in string(current_number)].^2)

            if ss_digits == 89
                cnt_89 += 1
                break
            elseif ss_digits == 1
                break
            end
        current_number = ss_digits
        end
    end
    return cnt_89
end 
euler92()
end
print(euler92())