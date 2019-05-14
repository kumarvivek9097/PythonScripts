## Problem Statement
In some bank each month we are required to maintain some "Monthly Average Balance" and on failing of which bank charges some amount. Sometime we failed to maintain this for initial some days of the month. Now to maintain MAB, we need to add some extra amount so that overall average balance will become equal to MAB. 
So this script will give answer to two problems:

 *  On failing to maintain MAB for some initial days, how much average balance is required for rest of month to maintain MAB
 *  If given some extra amount, for how many days you need to keep that extra amount in bank to maintain MAB
 
 ## Parameters
 Following *paramters* you must know to complete this script:
 -  `Monthly Average Balance`
 -  `Current MAB`
 -  `Current Balance`
 -  `Extra Amount to Add`

## Libraries 
Following libraries are used in this project:

- numpy
- math
- calendar
- datetime
- sympy
