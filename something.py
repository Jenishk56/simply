test = {}
test_new = {}
test["abc"] = {}
test_new["abc"] = {}

test["abc"]["a"] = 1
test["abc"]["b"] = 2
test["abc"]["c"] = 3

test_new["abc"]["a"] = 4

for test_key, test_value in test_new.items():
    for test_inner_key, test_inner_value in test_value.items():
        test[test_key][test_inner_key] = test_inner_value

print(test)
