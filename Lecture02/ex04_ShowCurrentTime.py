'''
Exercise04 - Show Current Time.

Chung Yuan Christian University
written by Woody Lo (the teaching assistant of Python Course_Summer Camp.)
'''
import time


##### First Method to Get Current Time #####
"""
Sencond and minute are sexagesimal-system (base-60) which is a numeral system with sixty as its base.
Hour is quadrovigesimal-system (base-24) which is a numeral system with twenty four as its base.
"""
currentTime01 = time.time()          # Get current time (float type).

# Obtain the total seconds since midnight, Jan 1, 1970.
totalSeconds = int(currentTime01)    # Convert the data tpye from float to int (turncate).

# Get the current second.
currentSecond = totalSeconds % 60    # Take the remainder of 'totalSeconds'.

# Obtain the total minites.
totalMinutes = totalSeconds // 60    # Take the quotient of 'totalSeconds'.

# Compute the current minute in the hour.
currentMinute = totalMinutes % 60    # Take the remainder of 'totalMinutes'.

# Obtain the total hours.
totalHours = totalMinutes // 60      # Take the quotient of 'totalMinutes'.

# Compute the current hour (Taiwan Time = GMT + 8).
currentHour = (totalHours + 8) % 24  # Take the remainder of 'totalHours'.

# Display result.
print("Current time is: ", str(currentHour), ":", str(currentMinute), ":", str(currentMinute),"(HH:MM:SS)")


##### Second Method to Get Current Time #####
currentTime02 = time.asctime( time.localtime(time.time()) )
print("Current time is: ", currentTime02)



'''
MATHEMATICS ENGLISH VOCABULARY

Addend	加數
Addition	加法
Algebra	代數
Arithmetic	算術, 四則運算
Calculation	計算
Common Denominator	共分母
Cube Root	立方根
Cube	三次方
Cubic Equation	三次方程式
Decimal Point	小數點
Derivative	導數
Differential Calculus	微分學
Dividend	被除數
Division	除法
Divisor	除數
Equation	等式,方程式
Exponent	指數
Fraction	分數
Function	函數
integral Calculus	積分
Logarithm Table	對數表
Logarithm	對數
Mathematics	數學
Minus Sign	減號
Multiplicand	被乘數
Multiplication	乘法
Multiplier	乘數
Nought Point Four	零點四
Numerator	分子
Operation	運算
Plus Sign	加號
Power	冪, 乘方
Product	積數
Proportion	比例
Quadratic Equation	二次方程
Quotient	商數
Ratio	比率/比
Remainder	餘數
Rule of three	比例法
Simple Equation	一次方程
Square root	平方根
Subtraction	減法
Sum	總和
Theorem	定理
Three cubed	三次方的
Unknown	未知數
x Squared	某數的平方
2 plus 1 equals 3	二加一等於三
4 minus 2 equals 2	四減二等於二
4 multiplied by 5, 4 times 5	四乘以五
Plus	加號；正號 +
Minus	減號；負號 -
Plus or Minus	正負號 ±
Multiplied	乘號 ×
Divided	除號 ÷
is Equal	等號 ＝
is not Equal	不等號 ≠
is Equivalent	全等於號 ≡
Less than	小於號 <
More than	大於號 >
Per cent	百分之 %
Per mill	千分之 ‰…
Infinity	無限大號 ∞
Square root	平方根 √ ∵
Union of	聯集 ∪
Intersection	交集 ∩
the Integral	的積分 ∫
pi	圓周率 π
Triangle	三角形 △
Perpendicular	垂直於 ⊥
'''