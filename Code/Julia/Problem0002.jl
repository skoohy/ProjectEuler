@time begin
function fib(N)
    if N == 0
        return 0
    end
    F = [big"1" big"1"; big"1" big"0"]^N
    return F[2]
end

function euler2()
    N = 0; ans = 0

    while fib(N) < 4000000
        if fib(N) % 2 == 0
            ans += fib(N)
        end
        N += 1
    end
    return ans
end
euler2()
end
print(euler2())