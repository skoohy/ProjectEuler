function euler5()
    N = 1
    while true
        divisors_count = 0
        for n in range(1, 20)
            if N % n == 0
                divisors_count += 1
            else
                N += 1
            end
        end
        if divisors_count == 20
            return N
        end
    end
end

print(euler5())