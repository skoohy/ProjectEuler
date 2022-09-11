@time begin     
function euler4()
    max_palindrome = 0
    for x in range(100, 999)
        for y in range(100, 999)
            num = x*y
            if num == parse(Int64, reverse(string(num))) && num > max_palindrome
                max_palindrome = num
            end
        end
    end

    return max_palindrome
end
euler4()
end
print(euler4())