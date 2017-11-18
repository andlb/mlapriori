# Machine learning - A Priori

Aprior - what is it all about?
When somebody bought also bought.

For example:
order             productis
10150             Burguer, french fries, vegetable
10151             Burguer, french fries
10152             Vegetables and fruits
10153             Burguer, pasta, French fries

When somebody buy burguer, they also buy french fries
Vegetable also buy fruits.


Algorithm has 3 parts: suport, confidence and lift.
suport is how many people has bought some product divided by the total of people who bought.
confidence is the number of people who bought product one and product two divided by the total of people who bought the product one.
lift confidence difided by the suport.

large datase, it is important to set a minimun for the confidence and support. The example set 20%.
Take the subset with the higher support
Take the subset with the higher confidence.
sort the rules by decrising the lift.

Sparse matrix: is a matrix where the most part of the elements are zero. If the most part of the elements are nonzero is considered densy.

