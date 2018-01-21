from RS.RSCoder import RSCoder
from RS.RSSimplifiedCoder import RSSimplifiedCoder
from RS.RSTestRunner import RSTestRunner

prim = 0x11d
# Code parameters for RS code with t = 6
n = 255
k = 243

rs = RSCoder(prim)
rs2 = RSSimplifiedCoder(prim)
test_runner = RSTestRunner(n, k)

errors = 1

success, fail, duration = test_runner.test(rs, errors, 100)

print("\n--- Results:---")
print("Success count: ", success)
print("Failure count: ", fail)
print("Percentage: ", (success/(success+fail))*100, "%")
print("Injected errors: ", errors)
print("Duration: ", duration)
