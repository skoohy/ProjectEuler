function euler33()
    numbers = []

    for x in range(10, 99)
        for y in range(10, 99)
            if x / y < 1
                x_digits = [parse(Int, a) for a in string(x)]
                y_digits = [parse(Int, a) for a in string(y)]

                for x_dig in x_digits
                    for y_dig in y_digits
                        if x_dig != 0
                            if y_dig != 0
                                if x_dig == y_dig
                                    deleteat!(x_digits, findfirst(x->x==x_dig, x_digits))
                                    deleteat!(y_digits, findfirst(y->y==y_dig, y_digits))

                                    new_x = x_digits[1]
                                    new_y = y_digits[1]

                                    if (new_x != 0) && (new_y != 0)
                                        if x/y == new_x / new_y
                                            push!(numbers, new_x/new_y)
                                        end
                                    end
                                end
                            end
                        end
                    end
                end
            end
        end
    end
    product = prod(numbers)
    
    return product
end                   

print(euler33())