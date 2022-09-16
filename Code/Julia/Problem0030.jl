@time begin
function euler30()
    ans = 0
    for n in range(2, 354294)
        if sum([parse(Int64, i) for i in string(n)].^5) == n
            ans += n
        end
    end
    return ans
end
euler30()
end
print(euler30())