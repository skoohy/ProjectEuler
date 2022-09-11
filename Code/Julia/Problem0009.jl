@time begin
function euler9()
    for a in range(1, 500)
        for b in range(a+1, 500)
            c = 1000 - b - a
            if a^2 + b^2 == c^2
                return a*b*c
            end
        end
    end
end
euler9()               
end 
print(euler9())           