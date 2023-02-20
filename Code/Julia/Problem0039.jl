using StatsBase

function euler39()
    perimeters = []; p = 1000

    for a in range(1, 500)
        for b in range(a, 500)
            c = sqrt(a^2 + b^2)
                if round(c) == c && a + b + c <= p
                    push!(perimeters, a+b+c)
                end
        end
    end
    return mode(perimeters)
end

print(euler39())