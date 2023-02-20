using Primes

function euler3(N = 600851475143)
    return maximum(factor(Set, N))
end

print(euler3())