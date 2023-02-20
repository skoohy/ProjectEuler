function fib(N)
    F_n = big"0"; F_n1 = big"1"; F_new = big"0"  
    i = 0

    if N == 0
        return F_n
    end

    if N == 1
        return F_n1
    end

    while i <= N-2
        F_new = F_n + F_n1
        F_n, F_n1 = F_n1, F_new
        i += 1
    end
    return F_new
end

function euler25(x=1000)
    N = 0
    while ndigits(fib(N)) < x
        N += 1
    end
    return N
end

print(euler25())
