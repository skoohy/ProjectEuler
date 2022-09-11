@time begin
function fib(N)
    if N == 0
        return 0
    end
    F = [big"1" big"1"; big"1" big"0"]^N
    return F[2]
end

function euler25(x = 1000)
    N = 0
    while ndigits(fib(N)) < x
        N += 1
    end
    return N
end
euler25()
end
print(euler25())
