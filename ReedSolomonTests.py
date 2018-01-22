from RS.RSCoder import RSCoder
from RS.RSSimplifiedCoder import RSSimplifiedCoder
from RS.RSTestRunner import RSTestRunner

prim = 0x11d
# Code parameters for RS code with t = 6
n = 255
k = 243

error_counts = [1, 2, 3, 4, 5, 8, 10, 12, 15, 20]

rs = RSCoder(prim)
rs2 = RSSimplifiedCoder(n-k, prim)
coders = [rs]

test_runner = RSTestRunner(n, k)


for err_count in error_counts:
    for coder in coders:

        with open('results.txt', 'a') as f:

            samples = 1000 if err_count < 10 else 5000

            success, fail, duration = test_runner.test(coder, err_count, samples)

            f.write("\n\n--- Results:---")
            f.write("\nCoder: ")
            f.write("Simplified" if coder is rs2 else "Normal")
            f.write("\nInjected errors: " + str(err_count))
            f.write("\nSuccess count: " + str(success))
            f.write("\nFailure count: " + str(fail))
            f.write("\nPercentage: " + str((success/(success+fail))*100) + "%")
            f.write("\nDuration: " + str(duration))

