from RS.RSCoder import RSCoder
from RS.RSTestRunner import RSTestRunner

prim = 0x11d
n = 15
k = 7

rs = RSCoder(prim)
test_runner = RSTestRunner(n, k)

errors = 9

success, fail, duration = test_runner.test(rs, errors, 10000)

print("\n--- Results:---")
print("Success count: ", success)
print("Failure count: ", fail)
print("Percentage: ", (success/(success+fail))*100, "%")
print("Injected errors: ", errors)
print("Duration: ", duration)
