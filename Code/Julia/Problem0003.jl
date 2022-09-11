@time begin
using Primes

function euler3(N = 600851475143)
    return maximum(factor(Set, N))
end
euler3()
end
print(euler3())