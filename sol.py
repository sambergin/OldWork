from pyspark.mllib.regression import LinearRegressionWithSGD
from pyspark.mllib.util import MLUtils
from pyspark import SparkContext
from numpy import array
from pyspark.mllib.linalg import Vectors

sc = SparkContext()

data = MLUtils.loadLibSVMFile(sc, "C:\\Users\\sambe\\Desktop\\422a3\\train_scaled.txt")


mod = LinearRegressionWithSGD.train(data, iterations = 100, intercept = True)

w = "Weights: " + str(mod.weights)
i = "Intercept: " + str(mod.intercept)
print(w)

print(i)


vec = array([0.343158, 0.762712, -0.27243, 0.678756, -0.0348259, 0.163445, -0.00635324, -0.295056, -0.396509, 0.142857, -0.256757, -0.118812, 0.294964, 0.821429])

p = mod.predict(vec)

print("prediction: ")

print(p)