# Mutation_Testing

# Introduction
  First I uploaded both Polynomial.py and PolyTest. For the Mutation Testing it will check and see what works and what doesn't I will then try to modify certain arithmetic symbols and see how it affects the software. 

# List of defined mutation operators

  I mutated the addition and subtraction operations to make it mutiplication, division, addition, and subtraction (the opposite depending on the function) from scratch. I commented it out and test each one and it clearly didn't pass the assert test which means it has successfully identified the mutation. 

# Description of applied mutations and their impact

  Each mutation does a specific arethmetic that is not intended for the function. For example the addition function should add the polynomials, not subtract, multiply, or divide the polynomial. After doing the assert it failed the test for each mutation because it checked to see if the addidtion added correctly and if the subtration subtracted correctly.

# Summary of mutant survival and killing

   All the mutations I created and tested failed because it didn't pass the assert.
   
# Analysis of the test suite's effectiveness

I could have added more test examples because there will be some cases where the mutation test cases won't successfully catch the mutation due to the kind of operation. For example adding a 2 + 2 and doing 2 * 2 both give you 4 or 100 - 0 and 100 + 0 still gives you 100. Besides these special cases the test suite's effectiveness is 

# Recommendations for improving the test suite

  A way to improve the test suite is by adding more test examples and trying to account for the special cases. 

# Conclusion

  I learned how to implement mutation testing and see what passed and what failed. I found out how testing can improve your data structure and how the smallest change in the code can destory everything. I will now submit a zip :)
